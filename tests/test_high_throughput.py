import json
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest.mock import Mock, patch

import requests
import academic
import conference_meta
import fetch_util
import nature_meta


class HighThroughputTests(unittest.TestCase):
    def test_interrupted_source_is_resumed_before_new_sources(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root = Path(tmp)
            (root / '2024').mkdir()
            (root / '2024/run-status.json').write_text('[{"source":"interspeech","state":"running"}]')
            argv = ['academic.py', '-v', 'wacv,interspeech,nature', '-y', '2024', '--metadata-only',
                    '--skip-completed', '--metadata-dir', tmp]
            with patch('sys.argv', argv), patch('academic.crawl_metadata_venue') as crawl, \
                    patch('academic.write_merged'):
                academic.main()
            self.assertEqual(crawl.call_args_list[0].args[0], 'interspeech')

    def test_journal_details_overlap_but_checkpoints_stay_on_source_thread(self):
        barrier = threading.Barrier(2)
        owner = threading.get_ident()
        written_by = []
        def detail(*args, **kwargs):
            barrier.wait(timeout=2)
            return '<meta name="citation_abstract" content="A real abstract."><meta name="citation_article_type" content="Article">'
        items = [{'DOI': f'10.1038/test{i}', 'title': [f'Paper {i}'],
                  'published-online': {'date-parts': [[2024, 1, 1]]}} for i in range(2)]
        with patch('nature_meta.resolve_issn', return_value='1234-5678'), \
                patch('nature_meta.get_json', return_value={'message': {'items': items}}), \
                patch('nature_meta.get_text', side_effect=detail):
            rows = nature_meta.crawl_nature('nature', 2024, 2, {}, lambda row: written_by.append(threading.get_ident()))
        self.assertTrue(all(row['abstract'] == 'A real abstract.' for row in rows))
        self.assertEqual(written_by, [owner, owner])

    def test_skips_completed_sources_without_changing_saved_records(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root = Path(tmp)
            folder = root / 'cvpr/2024'
            folder.mkdir(parents=True)
            (folder / 'papers.json').write_text('[{"id":"keep"}]')
            (folder / 'ai4s.json').write_text('[]')
            (root / '2024').mkdir()
            (root / '2024/run-status.json').write_text('[{"source":"cvpr","state":"completed"}]')
            argv = ['academic.py', '-v', 'cvpr,wacv', '-y', '2024', '--metadata-only',
                    '--workers', '16', '--skip-completed', '--metadata-dir', tmp]
            with patch('sys.argv', argv), patch('academic.crawl_metadata_venue') as crawl, \
                    patch('academic.write_merged'):
                academic.main()
            self.assertEqual([call.args[0] for call in crawl.call_args_list], ['wacv'])
            self.assertEqual(json.loads((folder / 'papers.json').read_text()), [{'id': 'keep'}])

    def test_scheduling_interleaves_journals_and_conferences(self):
        result = academic.schedule_venues(['ppopp', 'fast', 'nature', 'iclr', 'natcomputsci'])
        self.assertEqual(result, ['iclr', 'ppopp', 'nature', 'fast', 'natcomputsci'])

    def test_iccv_2024_is_not_requested_as_a_real_event(self):
        with patch('academic.crawl_openaccess_metadata') as fetch:
            self.assertEqual(academic._crawl_one_metadata('iccv', 2024, None, {}, lambda r: None), [])
            fetch.assert_not_called()

    def test_official_publisher_abstract_selectors(self):
        for selector in ('article__abstract', 'acl-abstract', 'field-name-field-paper-description'):
            html = '<div class="' + selector + '">A genuine paper abstract.</div>'
            self.assertEqual(conference_meta.parse_publisher_abstract(html), 'A genuine paper abstract.')

    def test_large_dblp_detail_query_splits_on_transient_failure(self):
        rows = [{'pub': {'value': 'https://dblp.org/rec/conf/test/' + str(i)},
                 'title': {'value': 'Paper ' + str(i)}} for i in range(2)]
        error = requests.HTTPError(response=Mock(status_code=502))
        replies = [error, {'results': {'bindings': [rows[0]]}}, {'results': {'bindings': [rows[1]]}}]
        with patch('conference_meta.get_json', side_effect=replies) as get:
            result = conference_meta._details(rows)
        self.assertEqual([r['pub'] for r in result], [r['pub'] for r in rows])
        self.assertEqual(get.call_count, 3)

    def test_paper_detail_pool_overlaps_work_and_preserves_order(self):
        barrier = threading.Barrier(4)
        def work(value):
            barrier.wait(timeout=2)
            return value * 2
        self.assertEqual(list(fetch_util.map_details(work, range(4))), [0, 2, 4, 6])

    def test_one_source_does_not_queue_its_entire_page_before_other_sources(self):
        produced = []
        def many():
            for value in range(1000):
                produced.append(value)
                if len(produced) > 8:
                    raise AssertionError('Source consumed too much work before yielding a result')
                yield value
        iterator = fetch_util.map_details(lambda value: value, many())
        try:
            self.assertEqual(next(iterator), 0)
            self.assertLessEqual(len(produced), 8)
        finally:
            iterator.close()

    def test_openalex_allows_two_inflight_requests_without_holding_rate_lock(self):
        barrier = threading.Barrier(2)
        response = Mock(status_code=200, headers={})
        def transport(*args, **kwargs):
            barrier.wait(timeout=2)
            return response
        with patch.dict(fetch_util._NEXT_ALLOWED, {}, clear=True), \
                patch('fetch_util._session_get', side_effect=transport), \
                patch('fetch_util.time.sleep'):
            with ThreadPoolExecutor(max_workers=2) as pool:
                futures = [pool.submit(fetch_util.request_get, 'https://api.openalex.org/works') for _ in range(2)]
                self.assertTrue(all(f.result() is response for f in futures))


if __name__ == '__main__':
    unittest.main()
