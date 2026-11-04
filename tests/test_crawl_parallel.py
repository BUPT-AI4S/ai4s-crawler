import json
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

import academic
from conference_meta import crawl_conference


class ParallelCrawlTests(unittest.TestCase):
    def test_supported_openreview_source_is_scheduled_first(self):
        argv = ['academic.py', '-v', 'ppopp,iclr', '-y', '2024', '--metadata-only']
        with patch('sys.argv', argv), patch('academic.crawl_metadata_venue') as crawl, \
                patch('academic.write_run_status'), patch('academic.write_merged'):
            academic.main()
        self.assertEqual(crawl.call_args_list[0].args[0], 'iclr')

    def test_four_sources_overlap_and_merge_only_after_all_finish(self):
        barrier = threading.Barrier(4)
        completed = []
        def crawl(venue, *args):
            barrier.wait(timeout=3)
            completed.append(venue)
            return []
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            argv = ['academic.py', '-v', 'cvpr,wacv,ncs,nmi', '-y', '2024',
                    '--metadata-only', '--workers', '4', '--metadata-dir', tmp]
            with patch('sys.argv', argv), patch('academic.crawl_metadata_venue', side_effect=crawl), \
                    patch('academic.write_merged') as merge:
                academic.main()
            self.assertEqual(len(completed), 4)
            merge.assert_called_once()
            status = json.loads((Path(tmp) / '2024/run-status.json').read_text())
            self.assertTrue(all(row['state'] == 'completed' for row in status))

    def test_failure_does_not_cancel_other_sources_and_is_recorded(self):
        def crawl(venue, *args):
            if venue == 'cvpr':
                raise RuntimeError('upstream unavailable')
            return []
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            argv = ['academic.py', '-v', 'cvpr,wacv', '-y', '2024', '--metadata-only',
                    '--workers', '2', '--metadata-dir', tmp]
            with patch('sys.argv', argv), patch('academic.logger'), \
                    patch('academic.crawl_metadata_venue', side_effect=crawl) as crawl_mock, \
                    patch('academic.write_merged') as merge:
                with self.assertRaises(SystemExit) as result:
                    academic.main()
            self.assertEqual(result.exception.code, 1)
            self.assertEqual(crawl_mock.call_count, 2)
            merge.assert_called_once()
            status = {r['source']: r['state'] for r in json.loads((Path(tmp) / '2024/run-status.json').read_text())}
            self.assertEqual(status, {'cvpr': 'failed', 'wacv': 'completed'})


class BatchAbstractTests(unittest.TestCase):
    def test_batch_abstracts_backfill_cached_records_without_per_paper_requests(self):
        bindings = [{k: {'value': v} for k, v in {
            'pub': f'https://dblp.org/rec/conf/ppopp/Test{i}', 'title': f'Paper {i}',
            'doi': f'https://doi.org/10.1145/test{i}', 'year': '2024',
        }.items()} for i in range(2)]
        payload = {'results': {'bindings': bindings}}
        saved = []
        with patch('conference_meta.get_json', side_effect=[payload, payload]), \
                patch('conference_meta.openalex_abstracts', return_value={
                    '10.1145/test0': 'Abstract zero.', '10.1145/test1': 'Abstract one.'}) as batch, \
                patch('conference_meta.crossref_abstract') as crossref, \
                patch('conference_meta.publisher_abstract') as publisher:
            rows = crawl_conference('ppopp', 2024, None,
                                    {'10.1145/test0': {'id': '10.1145/test0', 'abstract': None}}, saved.append)
        batch.assert_called_once_with(['10.1145/test0', '10.1145/test1'])
        crossref.assert_not_called()
        publisher.assert_not_called()
        self.assertEqual(len(saved), 2)
        self.assertTrue(all(row['abstract'] and row['screening_status'] == 'ready' for row in rows))
        self.assertTrue(all('openalex' in row['source'] for row in rows))


if __name__ == '__main__':
    unittest.main()
