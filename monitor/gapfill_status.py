"""Publish only safe progress fields from the current gapfill systemd job."""
import json
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

from monitor_server import read_counts


def service():
    output = subprocess.check_output(
        ['systemctl', 'show', 'gapfill.service', '-p', 'MainPID', '-p', 'ActiveState',
         '-p', 'InvocationID'], text=True, timeout=5
    )
    return dict(line.split('=', 1) for line in output.splitlines())


def terminal_states(lines):
    result = {}
    for line in lines:
        match = re.match(r'^(DONE|FAIL) (j-[a-f0-9]+)(?: |$)', line)
        if match:
            result[match[2]] = 'done' if match[1] == 'DONE' else 'failed'
    return result


def main(root):
    info = service()
    if info['ActiveState'] != 'active' or not re.fullmatch(r'[0-9a-f]{32}', info['InvocationID']):
        raise SystemExit('No active gapfill invocation')
    command = Path(f'/proc/{int(info["MainPID"])}/cmdline').read_bytes().decode().split('\0')
    sources = list(dict.fromkeys(arg for arg in command if re.fullmatch(r'j-[a-f0-9]+', arg)))
    if not sources or '/tmp/gap_backfill.py' not in command:
        raise SystemExit('Unexpected gapfill process')

    dest = root / 'backfill-jobs.json'
    try:
        previous = json.loads(dest.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        previous = {}
    if [job['source'] for job in previous.get('folders', [])] == sources:
        payload = previous
    else:
        payload = {'started_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                   'folders': [{'source': source,
                                'missing_start': read_counts(root / source / '2024' / 'papers.json')[2]}
                               for source in sources]}
    folders = payload['folders']
    invocation = info['InvocationID']
    while True:
        current = service()
        active = current['InvocationID'] == invocation and current['ActiveState'] == 'active'
        lines = subprocess.check_output(
            ['journalctl', '--no-pager', '-o', 'cat', '_SYSTEMD_INVOCATION_ID=' + invocation],
            text=True, errors='replace', timeout=8
        ).splitlines()
        terminal = terminal_states(lines)
        started = {m[1] for line in lines if (m := re.fullmatch(r'START (j-[a-f0-9]+)', line))}
        waiting = [source for source in sources if source not in terminal]
        for folder in folders:
            source = folder['source']
            folder['status'] = terminal.get(source, (
                'running' if source in (started or waiting[:3]) else 'queued') if active else 'stopped')
        temp = dest.with_suffix('.json.tmp')
        temp.write_text(json.dumps(payload), encoding='utf-8')
        temp.chmod(0o644)
        temp.replace(dest)
        if not active:
            break
        time.sleep(15)


if __name__ == '__main__':
    main(Path(sys.argv[1]))
