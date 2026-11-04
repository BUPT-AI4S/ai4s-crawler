"""Apply the monitor retry-visibility upgrade to deployed monitor files.

Idempotent: every anchor is asserted, and already-applied files are skipped.
"""
import shutil
import sys
from pathlib import Path

ROOT = Path('/home/academic/monitor')
BACKUP = Path('/mnt/figure/academic/archive/monitor-20261104')

SERVER_PY = r'''
RETRY_ENTRY = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\.\d+ \| WARNING\s+\| '
                         r'conference_meta:_page_payload:\d+ - (\S+) \d{4}: DBLP 枚举第 (\d+) 次失败（(.+?)），')
RETRY_ROUND = re.compile(r'第 (\d+) 轮重试上游暂时不可用的来源（(\d+) 个）: (.+)$')
RETRY_GIVEUP = re.compile(r'以下来源上游持续不可用，已保留断点、下次运行优先重试: (.+)$')


def retry_evidence(lines):
    """Collect per-source upstream retry attempts from the crawler log tail."""
    evidence, round_no, waiting = {}, None, []
    for line in lines:
        match = RETRY_ENTRY.match(line)
        if match:
            stamp, source, attempt, error = match.groups()
            evidence[source] = {'attempt': int(attempt), 'error': error, 'at': stamp,
                                'epoch': _local_epoch(stamp)}
            continue
        match = RETRY_ROUND.search(line)
        if match:
            round_no = int(match.group(1))
            continue
        match = RETRY_GIVEUP.search(line)
        if match:
            waiting = [name.strip() for name in match.group(1).split(',') if name.strip()]
    return evidence, round_no, waiting


def _local_epoch(stamp):
    try:
        return datetime.strptime(stamp, '%Y-%m-%d %H:%M:%S').timestamp()
    except ValueError:
        return 0.0


'''

RETRY_SCAN = '''        retries, retry_round, retry_waiting = retry_evidence(lines)
        now_epoch = time.time()
'''

RETRY_ROW = '''
                retry = retries.get(source)
                if retry:
                    row['retry_attempt'] = retry['attempt']
                    row['retry_error'] = retry['error']
                    row['retry_at'] = retry['at']
                    fresh = not retry['epoch'] or now_epoch - retry['epoch'] <= 3600
                    if fresh and (state == 'running' or task_states.get(source) == 'retryable'):
                        row['status'] = 'retrying'
                if task_states.get(source) == 'retryable':
                    row['status'] = 'retrying'
'''

RETRYING_ROWS = """        retrying = [row for row in rows if row['status'] == 'retrying']
"""

RETRY_FIELDS = """                'retrying_sources': [{'source': row['source'], 'title': row['title'],
                                      'attempt': row.get('retry_attempt'), 'error': row.get('retry_error'),
                                      'at': row.get('retry_at'), 'papers': row['papers'],
                                      'abstracts': row['abstracts'], 'updated': row['updated']}
                                     for row in retrying],
                'retry_round': retry_round, 'retry_waiting': retry_waiting,
"""

APP_STATES = """const sourceStates = {collecting:'采集中',retrying:'上游抖动 · 重试中',completed:'已生成结果',failed:'采集失败',pending:'等待采集',unreadable:'文件暂不可读',not_held:'该年未举办'};
let latest = null;
let fetching = false;

function renderRetries() {
  if (!latest) return;
  const rows = latest.retrying_sources || [];
  const section = $('retry-section');
  section.hidden = !rows.length;
  if (!rows.length) return;
  const attempt = row => Number.isFinite(row.attempt) ? `第 ${row.attempt} 次` : '—';
  const fragment = document.createDocumentFragment();
  for (const row of rows.slice().sort((a,b) => (b.attempt || 0) - (a.attempt || 0))) {
    const tr = document.createElement('tr');
    const values = [row.title || row.source, sourceStates.retrying, attempt(row), row.error || '—',
                    number(row.papers), number(row.abstracts), clock(row.updated)];
    values.forEach((value,index) => {
      const td = document.createElement('td');
      td.textContent = value;
      if (index === 0) td.title = `来源编号：${row.source}`;
      if (index === 1) td.className = 'status-retrying';
      if (index >= 4 && index <= 5) td.className = 'number';
      tr.append(td);
    });
    fragment.append(tr);
  }
  $('retry-sources').replaceChildren(fragment);
  const round = latest.retry_round;
  $('retry-round').textContent = [rows.length + ' 个来源', round ? `已进入第 ${round} 轮重试` : '第 1 轮退避重试中',
    latest.retry_waiting && latest.retry_waiting.length ? `${latest.retry_waiting.length} 个等待下次运行` : ''].filter(Boolean).join(' · ');
}
"""

HTML_SECTION = """  <section id="retry-section" aria-labelledby="retry-title" hidden>
    <div class="section-heading"><h2 id="retry-title">上游抖动 · 重试中的来源</h2><span id="retry-round" class="subtle"></span></div>
    <div class="table-wrap"><table><thead><tr><th scope="col">来源</th><th scope="col">状态</th><th scope="col">第几次重试</th><th scope="col">最近错误</th><th scope="col" class="number">论文</th><th scope="col" class="number">含摘要</th><th scope="col">最后写入</th></tr></thead><tbody id="retry-sources"><tr><td colspan="7" class="empty">正在读取重试状态…</td></tr></tbody></table></div>
    <p id="retry-note" class="hint">DBLP SPARQL 间歇性 503 / 超时：采集端会按 10→20→40… 秒退避重试，断点保留，不会直接判来源失败；重试仍不行会进入后续重试轮，最后才标记失败。</p>
  </section>
"""

CSS_EXTRA = """.status-retrying{color:#8a5a00;font-weight:600}
#retry-section .table-wrap table{min-width:700px}
#retry-round{font-variant-numeric:tabular-nums}
"""


def patch(text, anchor, replacement, label):
    if replacement.strip() and replacement.strip() in text:
        return text, False
    if text.count(anchor) != 1:
        raise SystemExit(f'anchor not unique for {label}: {text.count(anchor)}')
    return text.replace(anchor, replacement), True


def main():
    BACKUP.mkdir(parents=True, exist_ok=True)
    changed = []
    server = ROOT / 'monitor_server.py'
    text = server.read_text(encoding='utf-8')
    if not BACKUP.joinpath('monitor_server.py').exists():
        shutil.copy2(server, BACKUP / 'monitor_server.py')
    text, done = patch(text, 'def service_properties():', SERVER_PY + 'def service_properties():', 'server/functions')
    if done:
        changed.append('monitor_server.py')
    text, _ = patch(text, "        failed = set(re.findall(r' - (\\S+) 元数据抓取失败', '\\n'.join(lines)))",
                    RETRY_SCAN + "        failed = set(re.findall(r' - (\\S+) 元数据抓取失败', '\\n'.join(lines)))",
                    'server/scan')
    text, _ = patch(text, "                elif task_states.get(source) == 'pending':\n                    row['status'] = 'pending'",
                    "                elif task_states.get(source) == 'pending':\n                    row['status'] = 'pending'" + RETRY_ROW,
                    'server/row')
    text, _ = patch(text, "        return {'loading': False, 'year': year, 'updated_at': datetime.now(timezone.utc).isoformat(),",
                    RETRYING_ROWS + "        return {'loading': False, 'year': year, 'updated_at': datetime.now(timezone.utc).isoformat(),",
                    'server/retrying')
    text, _ = patch(text, "                'failed_sources': sum(row['status'] == 'failed' for row in rows),",
                    "                'failed_sources': sum(row['status'] == 'failed' for row in rows),\n" + RETRY_FIELDS,
                    'server/fields')
    server.write_text(text, encoding='utf-8')

    app = ROOT / 'app.js'
    text = app.read_text(encoding='utf-8')
    if not BACKUP.joinpath('app.js').exists():
        shutil.copy2(app, BACKUP / 'app.js')
    old_states = """const sourceStates = {collecting:'采集中',completed:'已生成结果',failed:'采集失败',pending:'等待采集',unreadable:'文件暂不可读',not_held:'该年未举办'};
let latest = null;
let fetching = false;
"""
    text, done = patch(text, old_states, APP_STATES, 'app/states')
    if done:
        changed.append('app.js')
    text, _ = patch(text, "  const rank = {collecting:0,failed:1,unreadable:2,completed:3,not_held:3,pending:4};",
                    "  const rank = {retrying:0,collecting:1,failed:2,unreadable:3,completed:4,not_held:4,pending:5};",
                    'app/rank')
    text, _ = patch(text,
                    "    const ai4s = row.ai4s_ready === false ? '待筛选' : number(row.ai4s) + (row.status === 'collecting' || row.status === 'failed' ? '（部分）' : '');",
                    "    const ai4s = row.ai4s_ready === false ? '待筛选' : number(row.ai4s) + (row.status === 'collecting' || row.status === 'retrying' || row.status === 'failed' ? '（部分）' : '');",
                    'app/ai4s')
    text, _ = patch(text, "  $('failed').textContent = number(data.failed_sources);",
                    "  $('failed').textContent = number(data.failed_sources);\n  $('retrying').textContent = number((data.retrying_sources || []).length);",
                    'app/metric')
    text, _ = patch(text, "  renderSources();\n}", "  renderSources();\n  renderRetries();\n}", 'app/render')
    app.write_text(text, encoding='utf-8')

    page = ROOT / 'index.html'
    text = page.read_text(encoding='utf-8')
    if not BACKUP.joinpath('index.html').exists():
        shutil.copy2(page, BACKUP / 'index.html')
    text, done = patch(text, 'style.css?v=20261104-names', 'style.css?v=20261104-retry', 'html/css')
    if done:
        changed.append('index.html')
    text, _ = patch(text, 'app.js?v=20261104-names', 'app.js?v=20261104-retry', 'html/js')
    text, _ = patch(text,
                    '      <div><dt>失败来源（近期日志）</dt><dd id="failed">—</dd></div>\n    </dl>',
                    '      <div><dt>失败来源（近期日志）</dt><dd id="failed">—</dd></div>\n'
                    '      <div><dt>重试中来源</dt><dd id="retrying">—</dd></div>\n    </dl>',
                    'html/metric')
    text, _ = patch(text, '  <section aria-labelledby="sources-title">',
                    HTML_SECTION + '  <section aria-labelledby="sources-title">', 'html/section')
    page.write_text(text, encoding='utf-8')

    style = ROOT / 'style.css'
    text = style.read_text(encoding='utf-8')
    if not BACKUP.joinpath('style.css').exists():
        shutil.copy2(style, BACKUP / 'style.css')
    if '.status-retrying' not in text:
        if not text.endswith('\n'):
            text += '\n'
        style.write_text(text + CSS_EXTRA, encoding='utf-8')
        changed.append('style.css')

    for name in ('monitor_server.py', 'app.js', 'index.html', 'style.css'):
        compile_ok = True
        if name.endswith('.py'):
            compile((ROOT / name).read_text(encoding='utf-8'), name, 'exec')
    print('语法检查通过；变更文件: ' + (', '.join(changed) or '无'))
    if 'monitor_server.py' not in changed:
        sys.exit('monitor_server.py 未变更，疑似锚点不匹配')


if __name__ == '__main__':
    main()
