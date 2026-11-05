import sys
from pathlib import Path

from academic import _folder_name, write_merged, write_run_status
from journal_abstract_backfill import _abstract_gap, complete_abstracts
from paper_record import load_records

year = int(sys.argv[1])
root = Path('/mnt/figure/academic/metadata')
states = {row['source']: row['state'] for row in load_records(root / str(year) / 'run-status.json')}
if not states:
    raise SystemExit('No bibliography status')
for row in load_records(root / str(year) / 'recovery-status.json'):
    source, state = row['source'], row['state']
    if states.get(source) == 'failed' and state in ('completed', 'abstract_incomplete'):
        states[source] = state

by_folder = {}
for venue, state in states.items():
    if state not in ('completed', 'abstract_queued', 'backfilling'):
        continue
    folder = _folder_name(venue)
    if _abstract_gap(root, year, folder)[0]:
        by_folder[folder] = venue
        states[venue] = 'abstract_queued'
write_run_status(root, year, states)

def update(folder, state):
    venue = by_folder[folder]
    if states[venue] != state:
        states[venue] = state
        write_run_status(root, year, states)

folders = list(by_folder)
print(f'{year}: queued {len(folders)} sources', flush=True)
for start in range(0, len(folders), 8):
    complete_abstracts(root, year, folders[start:start+8], update)
write_merged(root, year, states)
