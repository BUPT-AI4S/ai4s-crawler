import json
import tempfile
import unittest
import requests
from pathlib import Path
from unittest.mock import patch

import academic
from approved_sources import APPROVED_SOURCES
from nature_journals import JOURNALS
from journal_meta import crawl_journal


class TeacherCatalogTests(unittest.TestCase):
    @patch('journal_meta._queue_openalex_preview')
    @patch('journal_meta.get_json')
    def test_running_journal_applies_preview_before_later_pages(self, fetch, queue):
        from concurrent.futures import Future

        future = Future()
        future.set_result({'10.1/0': 'Preview abstract'})
        queue.side_effect = [future, None]
        page = [{'DOI': f'10.1/{i}', 'title': ['Paper']} for i in range(100)]
        fetch.side_effect = [
            {'message': {'items': page, 'next-cursor': 'page2'}},
            {'message': {'items': [{'DOI': '10.1/last', 'title': ['Last']}]}},
        ]
        saved = []
        rows = crawl_journal('example', 2024, None, {}, saved.append,
                             {'issns': ['1610-3653']}, defer_abstracts=True)
        self.assertEqual(rows[0]['abstract'], 'Preview abstract')
        self.assertEqual(rows[0]['source'], 'crossref.org+openalex.org')
        self.assertTrue(any(r.get('abstract') == 'Preview abstract' for r in saved))
    @patch('journal_meta.get_json')
    def test_restart_only_replays_unfinished_quarters(self, fetch):
        from journal_meta import crawl_journal_resumable
        from paper_record import RecordCheckpoint

        def page(doi):
            return {'message': {'items': [{'DOI': doi, 'title': ['Paper']}]}}

        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            dest = Path(tmp)
            checkpoint = RecordCheckpoint(dest / 'papers.json', resume=True)
            for i in range(200):
                checkpoint.add({'id': f'old/{i}'})
            fetch.side_effect = [page('10.1/first'), RuntimeError('interrupted')]
            with self.assertRaisesRegex(RuntimeError, 'interrupted'):
                crawl_journal_resumable('example', 2024, checkpoint.by_id, checkpoint.add,
                                        {'issns': ['1610-3653']}, checkpoint.flush, dest)
            resumed = RecordCheckpoint(dest / 'papers.json', resume=True)
            fetch.reset_mock()
            fetch.side_effect = [page('10.1/second'), page('10.1/third'), page('10.1/fourth')]
            rows = crawl_journal_resumable('example', 2024, resumed.by_id, resumed.add,
                                           {'issns': ['1610-3653']}, resumed.flush, dest)
            self.assertEqual([r['id'] for r in rows],
                             ['10.1/first', '10.1/second', '10.1/third', '10.1/fourth'])
            self.assertEqual(fetch.call_count, 3)
            self.assertIn('from-pub-date:2024-04-01', fetch.call_args_list[0].kwargs['params']['filter'])
    @patch('journal_meta.openalex_abstracts', return_value={})
    @patch('journal_meta.publisher_details', return_value={})
    @patch('journal_meta.get_json')
    def test_eccb_only_imports_official_supplement(self, fetch, details, abstracts):
        base={'title':['Protein design with machine learning'],'abstract':'Real abstract',
              'published-online':{'date-parts':[[2024,9,1]]},'volume':'40'}
        fetch.return_value={'message':{'items':[
            dict(base,DOI='10.1/eccb',issue='Supplement_2'),
            dict(base,DOI='10.1/other-conference',issue='Supplement_1')]}}
        rows=crawl_journal('eccb',2024,None,{},lambda row:None,{
            'issns':['1367-4803'],'volume':'40','issue':'Supplement_2',
            'venue_type':'conference','title':'ECCB'})
        self.assertEqual([r['id'] for r in rows], ['10.1/eccb'])
        self.assertEqual(rows[0]['venue_type'],'conference')

    def test_exact_workbook_selection_has_a_route_and_no_deferred_sources(self):
        raw = json.loads(Path('teacher_sources.json').read_text(encoding='utf-8'))
        selected = {r['code'] for r in raw['sources'] if r['recommendation'] == '建议纳入'}
        self.assertEqual(len(selected), 541)
        self.assertEqual(set(APPROVED_SOURCES), selected)
        self.assertEqual(len(selected & JOURNALS.keys()), 436)
        self.assertFalse(selected - academic.known_venues())
        self.assertNotIn('fast', selected)

    @patch('journal_meta.openalex_abstracts', return_value={})
    @patch('journal_meta.publisher_details', return_value={})
    @patch('journal_meta.get_json')
    def test_multi_issn_deduplicates_and_preserves_online_year(self, fetch, details, abstracts):
        item = {'DOI':'10.1/paper', 'title':['Deep learning for protein design'],
                'published-online':{'date-parts':[[2024,1,2]]},'abstract':'Real abstract'}
        future = dict(item, DOI='10.1/future', **{'published-online':{'date-parts':[[2025,1,1]]}})
        fetch.return_value = {'message':{'items':[item,future,item]}}
        saved=[]
        rows = crawl_journal('j-db72c3c601',2024,None,{},saved.append,
                             {'issns':['1610-3653','1610-3661']})
        self.assertEqual([r['id'] for r in rows], ['10.1/paper'])
        self.assertEqual(len(saved), 1)
        self.assertIn('until-pub-date:2024-12-31', fetch.call_args.kwargs['params']['filter'])
        self.assertIn('issn:1610-3653,issn:1610-3661', fetch.call_args.kwargs['params']['filter'])
        fetch.assert_called_once()
        details.assert_not_called()

    @patch('journal_meta.get_json', return_value={'message': {'items': [
        {'DOI': '10.1/paper', 'title': ['Paper']},
    ]}})
    def test_bibliography_is_checkpointed_before_abstract_enrichment(self, fetch):
        saved = []

        def abstracts(dois, openalex, **_kwargs):
            self.assertTrue(_kwargs.get('include_openaire'))
            self.assertEqual(saved[0]['screening_status'], 'needs_abstract')
            self.assertIsNone(saved[0]['abstract'])
            return {'10.1/paper': ('A real abstract', 'openalex.org')}

        with patch('journal_meta.fill_abstracts', side_effect=abstracts):
            rows = crawl_journal('example', 2024, None, {}, saved.append, {'issns': ['1610-3653']})
        self.assertEqual(saved[-1]['abstract'], 'A real abstract')
        self.assertIsNone(saved[0]['abstract'])
        self.assertEqual(rows[0]['abstract'], 'A real abstract')

    @patch('journal_meta.fill_abstracts')
    @patch('journal_meta.get_json', return_value={'message': {'items': [
        {'DOI': '10.1/paper', 'title': ['Paper']},
    ]}})
    def test_deferred_book_list_makes_no_abstract_requests(self, fetch, abstracts):
        rows = crawl_journal('example', 2024, None, {}, lambda row: None,
                             {'issns': ['1610-3653']}, defer_abstracts=True)
        self.assertEqual(rows[0]['screening_status'], 'needs_abstract')
        abstracts.assert_not_called()

    @patch.dict('os.environ', {'CROSSREF_COMPACT_SOURCE_YEARS': 'example:2024'})
    @patch('journal_meta.get_json', return_value={'message': {'items': []}})
    def test_compact_fields_are_scoped_to_the_audited_source_and_year(self, fetch):
        config = {'issns': ['1610-3653', '1610-3661']}
        crawl_journal('example', 2024, None, {}, lambda row: None, config)
        fields = fetch.call_args.kwargs['params']['select'].split(',')
        self.assertTrue({'ISSN', 'volume', 'issue', 'resource', 'abstract'} <= set(fields))
        crawl_journal('example', 2025, None, {}, lambda row: None, config)
        self.assertNotIn('select', fetch.call_args.kwargs['params'])

    @patch('journal_meta.get_json')
    def test_full_first_page_controls_later_field_selection(self, fetch):
        for subtype in (None, 'research-article'):
            first = [{'DOI': f'10.1/{i}', 'title': ['Paper'], 'subtype': subtype}
                     for i in range(100)]
            fetch.reset_mock()
            fetch.side_effect = [
                {'message': {'items': first, 'next-cursor': 'page2'}},
                {'message': {'items': [{'DOI': '10.1/last', 'title': ['Last']}],
                             'next-cursor': 'unused'}},
            ]
            rows = crawl_journal('example', 2024, None, {}, lambda row: None,
                                 {'issns': ['1610-3653']}, defer_abstracts=True)
            self.assertEqual(len(rows), 101)
            self.assertEqual(fetch.call_count, 2)
            self.assertNotIn('select', fetch.call_args_list[0].kwargs['params'])
            self.assertEqual('select' in fetch.call_args_list[1].kwargs['params'], subtype is None)

    @patch.dict('os.environ', {'CROSSREF_COMPACT_SOURCE_YEARS': 'example:2024'})
    @patch('journal_meta.get_json')
    def test_rejected_compact_request_retries_same_cursor_with_full_fields(self, fetch):
        response = requests.Response()
        response.status_code = 400
        fetch.side_effect = [requests.HTTPError(response=response), {'message': {'items': []}}]
        crawl_journal('example', 2024, None, {}, lambda row: None, {'issns': ['1610-3653']})
        first, retry = [call.kwargs['params'] for call in fetch.call_args_list]
        self.assertIn('select', first)
        self.assertNotIn('select', retry)
        self.assertEqual(first['cursor'], retry['cursor'])

    def test_selected_annual_merge_excludes_historical_disabled_sources(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as temp:
            root = Path(temp)
            for source in ('cvpr','fast'):
                folder=root/source/'2024'
                folder.mkdir(parents=True)
                (folder/'papers.json').write_text(json.dumps([{'id':source}]))
                (folder/'ai4s.json').write_text('[]')
            academic.write_merged(root,2024,['cvpr'])
            merged=json.loads((root/'2024/papers.json').read_text())
            self.assertEqual([r['id'] for r in merged], ['cvpr'])


if __name__ == '__main__':
    unittest.main()
