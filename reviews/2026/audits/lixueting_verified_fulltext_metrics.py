"""Publish the five content-reviewed AI4S decisions without inventing abstracts.

Only Li Xueting's named 2026 records qualify. The pinned monitor's complete
proof validator is reused; stale, conflicting, or incomplete records stay missing.
Original missingness remains in a separate field and in the original records.
"""
import argparse
import copy
import importlib.util
import json
from collections import Counter, defaultdict
from pathlib import Path

OWNER = '\u674e\u96ea\u5a77'
YEAR = 2026
CHECKED_AT = '2026-11-19T10:04:37.286434+00:00'
RECORDS = [
    {
        'id': '10.1016/s1474-4422(25)00453-3', 'venue': 'j-af35c70bf5',
        'scientific_task': 'Synthesis of epilepsy treatment-response and EEG biomarker research.',
        'ai_role': 'Substantively reviews SpikeNet2 training data, expert comparison and false detections, rather than merely proposing future AI use.',
        'evidence_location': 'Original publisher text, printed pp16 and18; p17 not read. On p18 the epilepsy discussion ends above the next article heading.',
        'evidence_urls': ['https://www.sciencedirect.com/science/article/pii/S1474442225004533', 'https://www.sciencedirect.com/science/article/pii/S147444222500448X'],
        'document_type_basis': 'Substantive short annual research review; evaluates completed scientific AI research.',
    },
    {
        'id': '10.1016/j.chmed.2026.08.014', 'venue': 'j-a847fdc23a',
        'scientific_task': 'Identify active bufadienolides and investigate the PDE4D target in experimental pharyngitis.',
        'ai_role': 'Support vector regression in QMDH links concentrations in 24 batches with anti-inflammatory activity; marker discovery precedes biochemical and animal validation.',
        'evidence_location': 'Original body, pharmacodynamic marker discovery paragraph and Figure1; direct To the Editor research text.',
        'evidence_urls': ['https://pmc.ncbi.nlm.nih.gov/articles/PMC13712334/'],
        'document_type_basis': 'Short original experimental research, despite its Letter format; not a reader comment.',
    },
    {
        'id': '10.1016/j.jchf.2025.102851', 'venue': 'j-896c5ba968',
        'scientific_task': 'Construct clinical presentation data from global DELIVER heart-failure trial records.',
        'ai_role': 'o1-mini extracts 51 variables, checked against human review in125 dossiers and applied to1237 hospitalization dossiers.',
        'evidence_location': 'Original manuscript INTRODUCTION, METHODS, RESULTS and central illustration.',
        'evidence_urls': ['https://pmc.ncbi.nlm.nih.gov/articles/PMC12949679/'],
        'document_type_basis': 'Original clinical AI methods and validation study.',
    },
    {
        'id': '10.1016/j.jchf.2026.103161', 'venue': 'j-896c5ba968',
        'scientific_task': 'Predict future clinical heart failure from baseline echocardiographic measurements.',
        'ai_role': 'AI-LVD is applied blinded to NIL-CHF baseline reports and evaluated against later heart-failure outcomes and PREVENT-HF.',
        'evidence_location': 'Publisher original Methods, Results and Discussion; formal volume14 issue10.',
        'evidence_urls': ['https://www.jacc.org/doi/10.1016/j.jchf.2026.103161'],
        'document_type_basis': 'Brief Report with original clinical cohort methods and results.',
    },
    {
        'id': '10.1016/j.jchf.2026.103188', 'venue': 'j-896c5ba968',
        'scientific_task': 'Detect impending NT-proBNP-defined worsening heart failure from wearable physiology.',
        'ai_role': 'Software-locked XGBoost uses heart-rate-derived signals, with91 derivation and33 temporal-validation participants and no validation retraining.',
        'evidence_location': 'Publisher original Methods, Results and Figure1; formal volume14 issue11.',
        'evidence_urls': ['https://www.jacc.org/doi/10.1016/j.jchf.2026.103188'],
        'document_type_basis': 'Original clinical prediction research; biomarker detection is not claimed to prove prevention of hospitalizations.',
    },
]


def has_text(value):
    return isinstance(value, str) and bool(value.strip())


def resolve_metrics(data, reviews, candidates, validator):
    """Return an owner-scoped derived copy and a transparent content audit."""
    result = copy.deepcopy(data)
    year = next(y for y in result['years'] if y['year'] == YEAR)
    sources = {s['code']: s for s in year['sources'] if s['owner'] == OWNER}
    candidate_map = {(r.get('venue'), r.get('id')): r for r in candidates if r.get('year') == YEAR}
    review_map = defaultdict(list)
    for record in reviews:
        if record.get('year') == YEAR:
            review_map[(record.get('venue'), record.get('id'))].append(record)
    qualified = Counter()
    audits = []
    for manifest in RECORDS:
        key = (manifest['venue'], manifest['id'])
        source, candidate, matches = sources.get(key[0]), candidate_map.get(key), review_map[key]
        valid = False
        if source and candidate and len(matches) == 1:
            record = matches[0]
            review = record.get('ai4s_review', {})
            metadata = review.get('verified_metadata', {})
            valid = (review.get('owner') == OWNER
                     and review.get('snapshot_at') == source.get('snapshot_at')
                     and review.get('decision') == 'include'
                     and not any(has_text(a) for a in (candidate.get('abstract'), record.get('abstract'), metadata.get('abstract')))
                     and candidate.get('abstract_requirement') == review.get('abstract_requirement')
                     and validator(review, OWNER))
        row = dict(manifest, year=YEAR, decision='include', checked_at=CHECKED_AT,
                   original_has_no_standalone_abstract=True,
                   review_basis='original_body_content', proof_accepted=bool(valid))
        if matches:
            row['title'] = matches[0].get('title')
        audits.append(row)
        if valid:
            qualified[key[0]] += 1
    for code, source in sources.items():
        # Preserve physical nulls. Only a validated identity-specific proof changes
        # the actionable display metric; any additional missing record remains open.
        physical = source.get('final_originally_missing_abstract', source.get('final_missing_abstract'))
        count = qualified[code]
        if type(physical) is not int or not count:
            continue
        if count > physical or count > source.get('abstract_full_text_reviewed', 0):
            raise ValueError('Full-text evidence does not reconcile with monitor counts: ' + code)
        source['final_originally_missing_abstract'] = physical
        source['final_no_abstract_full_text_reviewed'] = count
        source['final_missing_abstract'] = physical - count
        source['final_abstract_metric_basis'] = 'Unresolved included abstracts; original publisher-no-abstract records with validated body evidence are reported separately.'
        note = '\u539f\u6587\u65e0\u72ec\u7acb\u6458\u8981' + str(count) + '\u7bc7\uff0c\u5df2\u4f9d\u636e\u6b63\u6587\u6838\u5b9eAI4S\u5e76\u4fdd\u7559\u7eb3\u5165\uff1b\u6458\u8981\u539f\u59cb\u7a7a\u503c\u4fdd\u7559\uff0c\u4e0d\u518d\u8ba1\u4f5c\u7eb3\u5165\u7f3a\u6458\u8981\u5f85\u529e\u3002'
        if note not in source.get('coverage_note', ''):
            source['coverage_note'] = source.get('coverage_note', '') + '\n' + note
    audit = {'owner': OWNER, 'year': YEAR, 'checked_at': CHECKED_AT,
             'decision_counts': {'include': len(RECORDS), 'exclude': 0},
             'owner_instruction': 'Keep papers whose body demonstrates substantive AI4S; remove non-AI4S from inclusion. Do not show completed original-no-abstract cases as included-missing-abstract work.',
             'abstract_policy': 'Original abstract fields remain null. AI-written summaries and body introductions are never relabeled as original abstracts.',
             'records': audits}
    return result, audit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path('.'))
    parser.add_argument('--monitor-tools', type=Path, required=True)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('verified_monitor', args.monitor_tools / 'tools/build_review_monitor.py')
    monitor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(monitor)
    read = lambda path: json.loads(path.read_text())
    path = args.repo / 'reviews/monitor-data.json'
    data, audit = resolve_metrics(read(path), read(args.repo / 'reviews/2026/zch66883-lixueting.json'),
        read(args.repo / 'metadata/2026/ai4s.json'), monitor.full_text_abstract_exemption)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    (args.repo / 'reviews/2026/lixueting-no-abstract-content-review.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n')
    print('Content-reviewed original-no-abstract records accepted:', sum(r['proof_accepted'] for r in audit['records']))


if __name__ == '__main__':
    main()
