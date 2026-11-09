'use strict';
const $ = id => document.getElementById(id);
const number = value => Number.isFinite(value) ? value.toLocaleString('zh-CN') : '—';
const clock = value => value ? new Intl.DateTimeFormat('zh-CN', {timeZone:'Asia/Shanghai',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:false}).format(new Date(value)) : '—';
const states = {running:'运行中',finished:'已结束',failed:'任务失败',inactive:'未运行',unknown:'状态未知'};
const sourceStates = {abstract_queued:'等待补摘要',backfilling:'补摘要中',abstract_incomplete:'补查结束 · 仍缺摘要',collecting:'采集中',retrying:'上游抖动 · 重试中',completed:'已生成结果',failed:'采集失败',pending:'等待采集',unreadable:'文件暂不可读',not_held:'该年未举办'};
const backfillStates = {running:'回填中',queued:'排队中',done:'本轮结束',failed:'回填失败',stopped:'已停止',idle:'未在队列'};
let latest = null;
let fetching = false;

function renderBackfill() {
  if (!latest) return;
  const data = latest.backfill;
  const section = $('backfill-section');
  const rows = (data && data.jobs) || [];
  section.hidden = !rows.length;
  if (!rows.length) return;
  const fragment = document.createDocumentFragment();
  for (const row of rows) {
    const tr = document.createElement('tr');
    const values = [row.title || row.source, backfillStates[row.status] || row.status,
                    number(row.missing_start), number(row.missing_now), number(row.filled),
                    Math.round((row.percent || 0) * 100) + '%', clock(row.updated)];
    values.forEach((value,index) => {
      const td = document.createElement('td');
      td.textContent = value;
      if (index === 0) td.title = `来源编号：${row.source}`;
      if (index === 1) td.className = 'status-' + row.status;
      if (index >= 2 && index <= 5) td.className = 'number';
      tr.append(td);
    });
    fragment.append(tr);
  }
  $('backfill-jobs').replaceChildren(fragment);
  const cache = data.cache;
  $('backfill-summary').textContent = [
    `${data.folders_done}/${rows.length} 本已完成`,
    `当前缺口 ${number(data.total_missing_now)} 条（起始 ${number(data.total_missing_start)}，已补 ${number(data.total_filled)}）`,
    cache && Number.isFinite(cache.rows) ? `摘要缓存 ${number(cache.rows)} 条` : '',
    data.started_at ? `统计起点 ${data.started_at}` : ''
  ].filter(Boolean).join(' · ');
}

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
    const status = row.status === 'queued' ? '待重跑' : (sourceStates[row.status] || sourceStates.retrying);
    const values = [row.title || row.source, status, attempt(row), row.error || '—',
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
  $('retry-round').textContent = [rows.length + ' 个来源', round ? `已进入第 ${round} 轮重试` : '',
    latest.retry_waiting && latest.retry_waiting.length ? `${latest.retry_waiting.length} 个等待下次运行` : ''].filter(Boolean).join(' · ');
}

function renderSourceRows(id, rows) {
  const fragment = document.createDocumentFragment();
  for (const row of rows) {
    const tr = document.createElement('tr');
    const ai4s = row.ai4s_ready === false ? '待筛选' : number(row.ai4s) + (row.status === 'collecting' || row.status === 'retrying' || row.status === 'failed' ? '（部分）' : '');
    const values = [row.title || row.source,sourceStates[row.status] || row.status,number(row.papers),number(row.abstracts),ai4s,clock(row.updated)];
    values.forEach((value,index) => {
      const td = document.createElement('td');
      td.textContent = value;
      if (index === 0) td.title = `来源编号：${row.source}`;
      if (index === 1) td.className = 'status-' + row.status;
      if (index >= 2 && index <= 4) td.className = 'number';
      tr.append(td);
    });
    fragment.append(tr);
  }
  if (!rows.length) {
    const tr = document.createElement('tr'), td = document.createElement('td');
    td.colSpan = 6; td.className = 'empty'; td.textContent = '没有匹配的来源'; tr.append(td); fragment.append(tr);
  }
  $(id).replaceChildren(fragment);
}

function renderSources() {
  if (!latest) return;
  const query = $('search').value.trim().toLowerCase();
  const rank = {abstract_queued:3,backfilling:1,abstract_incomplete:4,retrying:0,collecting:1,failed:2,unreadable:3,completed:4,not_held:4,pending:5};
  const rows = latest.sources.filter(row => `${row.source} ${row.title || ''}`.toLowerCase().includes(query)).sort((a,b) => rank[a.status]-rank[b.status] || (a.title || a.source).localeCompare(b.title || b.source));
  renderSourceRows('sources', rows);
}

function renderRecovery(data) {
  const rows = data.recovery_sources || [];
  $('recovery-section').hidden = !rows.length;
  if (rows.length) {
    $('recovery-summary').textContent = `${rows.filter(row => row.status === 'completed').length} / ${rows.length} 个来源已生成结果`;
    renderSourceRows('recovery-sources', rows);
  }
  const preload = data.abstract_preload;
  $('preload-section').hidden = !preload;
  if (preload) {
    const stage = preload.handed_off ? '首轮已交接给回写任务' : 'OpenAlex 首轮补查';
    $('preload-summary').textContent = `${stage} · 覆盖 ${number(preload.sources)} 个来源 · 已查 ${number(preload.queried)} / ${number(preload.dois)} 个 DOI · 命中 ${number(preload.hits)} 条`;
  }
}

function render(data) {
  if (data.loading) { $('current').textContent = '服务器正在生成第一份快照…'; return; }
  latest = data;
  const service = data.service;
  $('state').textContent = states[service.state] || service.state;
  $('state').className = 'state ' + service.state;
  $('updated').textContent = '更新于 ' + clock(data.updated_at);
  const activeSources = data.current_sources || (data.current_source ? [data.current_source] : []);
  const titles = new Map(data.sources.map(row => [row.source, row.title || row.source]));
  $('current').textContent = activeSources.length ? `并发来源（${activeSources.length}）：` + activeSources.slice(0,4).map(source => titles.get(source) || source).join('、') + (activeSources.length > 4 ? ' 等，完整列表见来源明细' : '') : (service.state === 'running' ? '任务运行中，等待下一个断点' : '任务已停止，请结合日志确认结果');
  $('completed').textContent = `${number(data.completed_sources)} / ${number(data.total_sources)} 个来源已处理`;
  $('progress').max = data.total_sources || 1;
  $('progress').value = data.completed_sources;
  $('papers').textContent = number(data.saved_papers);
  $('abstracts').textContent = number(data.papers_with_abstract);
  $('ai4s').textContent = number(data.ai4s_candidates);
  $('failed').textContent = number(data.failed_sources);
  $('retrying').textContent = number((data.retrying_sources || []).length);
  $('backfilled').textContent = data.backfill ? number(data.backfill.total_filled) : '—';
  $('missing').textContent = number(data.missing_with_doi);
  const memory = Number.isFinite(service.memory_bytes) ? (service.memory_bytes / 1024**2).toFixed(0) + ' MB' : '—';
  const hours = Number.isFinite(service.elapsed_seconds) ? (service.elapsed_seconds / 3600).toFixed(1) + ' 小时' : '—';
  const space = Number.isFinite(data.disk_available_bytes) ? (data.disk_available_bytes / 1024**3).toFixed(1) + ' GB' : '—';
  const memoryLimit = Number.isFinite(service.memory_limit_bytes) ? (service.memory_limit_bytes / 1024**3).toFixed(0) + ' GB' : '—';
  const cpuLimit = number(service.cpu_limit_cores);
  $('resources').textContent = `任务内存 ${memory} / ${memoryLimit} · CPU 上限 ${cpuLimit} vCPU · 已运行 ${hours} · 数据盘可用 ${space}`;
  $('warnings').textContent = `最近 ${data.logs.length} 行：警告 ${number(data.recent_warnings)} · 错误 ${number(data.recent_errors)}`;
  const log = $('logs'), follow = log.scrollTop + log.clientHeight >= log.scrollHeight - 30;
  log.textContent = data.logs.join('\n') || '暂时没有日志。';
  if (follow) log.scrollTop = log.scrollHeight;
  $('output-papers').textContent = data.outputs.papers;
  $('output-ai4s').textContent = data.outputs.ai4s;
  $('merge-note').textContent = data.annual_merge_exists ? '汇总文件已存在；任务仍在运行时，它不一定包含全部最新断点。' : '整批任务进入汇总步骤后生成；采集中先查看各来源断点。';
  $('notice').hidden = !data.monitor_error;
  $('notice').textContent = data.monitor_error ? '本次状态采样未成功，正在展示上次数据；将自动重试。' : '';
  renderSources();
  renderRetries();
  renderRecovery(data);
  renderBackfill();
}

async function refresh() {
  if (fetching) return;
  fetching = true; $('refresh').disabled = true;
  try {
    const response = await fetch('status', {cache:'no-store',signal:AbortSignal.timeout(10000)});
    if (!response.ok) throw new Error('HTTP ' + response.status);
    render(await response.json());
  } catch {
    $('notice').hidden = false;
    $('notice').textContent = '暂时无法连接监控服务，保留上次数据。请稍后点击刷新，或检查网络。';
  } finally { fetching = false; $('refresh').disabled = false; }
}
$('search').addEventListener('input',renderSources);
$('refresh').addEventListener('click',refresh);
document.addEventListener('visibilitychange',() => { if (!document.hidden) refresh(); });
setInterval(() => { if (!document.hidden) refresh(); },15000);
refresh();
