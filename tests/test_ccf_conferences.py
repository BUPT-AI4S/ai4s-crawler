import unittest
from unittest.mock import patch

import academic
from ai4s_filter import select_ai4s
from ccf_venues import CONFERENCES, expand_ccf_venues, annotate_ccf_record
from conference_meta import (build_query, build_details_query, crawl_conference, record_from_binding,
                             parse_publisher_abstract, publisher_abstract)


def binding(key='Paper25', title='Machine learning for protein design'):
    return {k: {'value': v} for k, v in {
        'pub': f'https://dblp.org/rec/conf/ijcai/{key}', 'title': title,
        'doi': 'https://doi.org/10.24963/ijcai.2025/1', 'year': '2025',
        'authors': '2:::B Li:::https://dblp.org/pid/2|||1:::A Wang:::https://dblp.org/pid/1',
        'toc': 'https://dblp.org/db/conf/ijcai/ijcai2025', 'pages': '1-9',
        'booktitle': 'IJCAI',
    }.items()}


def response(rows):
    return {'results': {'bindings': rows}}


class CCFTests(unittest.TestCase):
    def setUp(self):
        batch = patch('conference_meta.fill_abstracts', return_value={})
        batch.start()
        self.addCleanup(batch.stop)

    def test_complete_catalog_without_fse_collision(self):
        self.assertEqual(len(CONFERENCES), 190)
        self.assertEqual(sum(c['rank'] == 'A' for c in CONFERENCES.values()), 58)
        self.assertEqual(sum(c['rank'] == 'B' for c in CONFERENCES.values()), 132)
        self.assertEqual(len({c['field'] for c in CONFERENCES.values()}), 10)
        self.assertEqual(CONFERENCES['fse']['rank'], 'A')
        self.assertEqual(CONFERENCES['fse-crypto']['rank'], 'B')
        self.assertNotEqual(CONFERENCES['fse']['dblp_stream'], CONFERENCES['fse-crypto']['dblp_stream'])

    def test_groups_aliases_and_custom_openreview_id(self):
        self.assertEqual(len(expand_ccf_venues(['ccf-ab'])), 190)
        self.assertEqual(len(expand_ccf_venues(['ccf-a'])), 58)
        self.assertEqual(len(expand_ccf_venues(['ccf-b'])), 132)
        self.assertEqual(expand_ccf_venues(['SIGKDD', 'kdd', 'nips', 'neurips', 'ICLR.cc/2025/Conference']),
                         ['kdd', 'neurips', 'ICLR.cc/2025/Conference'])
        self.assertEqual(expand_ccf_venues(['FSE-crypto', 'FSE']), ['fse-crypto', 'fse'])
        self.assertEqual(expand_ccf_venues(['ACM MM', 'CODES+ISSS']), ['mm', 'codes-isss'])

    def test_annotate_venue_grade_is_not_paper_certification(self):
        row = annotate_ccf_record({'title': 'Title', 'track': 'main'}, 'ijcai')
        self.assertEqual(row['ccf_rank'], 'B')
        self.assertEqual(row['ccf_paper_status'], 'unverified')
        self.assertEqual(row['ccf_catalog_version'], '2026-v7')
        self.assertEqual(annotate_ccf_record({'track': 'findings'}, 'acl')['ccf_paper_status'], 'excluded')

    def test_query_is_scoped_paged_and_uses_typed_year(self):
        query = build_query('miccai', 2025, 100, 200)
        self.assertIn('https://dblp.org/streams/conf/miccai', query)
        self.assertIn('"2025"^^xsd:gYear', query)
        self.assertIn('OFFSET 200', query)
        self.assertIn('LIMIT 100', query)
        self.assertIn('ORDER BY ?pub', query)
        self.assertNotIn('GROUP_CONCAT', query)
        self.assertNotIn('OPTIONAL', query)
        with self.assertRaises(ValueError):
            build_query('not-a-conference', 2025, 100, 0)

    def test_delayed_proceedings_use_conference_toc_year(self):
        query = build_query('asiacrypt', 2024, 100, 0)
        self.assertIn('dblp:listedOnTocPage ?toc', query)
        self.assertIn('asiacrypt2024', query)
        self.assertNotIn('"2024"^^xsd:gYear', query)
        self.assertIn('[-/.]', query)
        row = binding()
        row['year'] = {'value': '2025'}
        record = record_from_binding(row, 'asiacrypt', 2024)
        self.assertEqual(record['year'], 2024)
        self.assertEqual(record['published'], '2025')

    def test_detail_query_only_fetches_selected_records(self):
        pub = 'https://dblp.org/rec/conf/ijcai/Test25'
        query = build_details_query([pub])
        self.assertIn(f'VALUES ?pub {{ <{pub}> }}', query)
        self.assertNotIn('GROUP_CONCAT', query)
        with self.assertRaises(ValueError):
            build_details_query(['https://example.com/injected>'])

    def test_record_parsing_authors_doi_and_missing_abstract(self):
        row = record_from_binding(binding(), 'ijcai', 2025)
        self.assertEqual(row['id'], '10.24963/ijcai.2025/1')
        self.assertEqual(row['authors'], ['A Wang', 'B Li'])
        self.assertEqual(row['author_ids'], ['https://dblp.org/pid/1', 'https://dblp.org/pid/2'])
        self.assertEqual(row['screening_status'], 'needs_abstract')
        self.assertEqual(row['ccf_paper_status'], 'unverified')
        self.assertIsNone(row['pdf_url'])
        no_doi = binding(); no_doi.pop('doi')
        self.assertEqual(record_from_binding(no_doi, 'ijcai', 2025)['id'], no_doi['pub']['value'])
        no_doi['document'] = {'value': 'https://proceedings.mlr.press/v291/example.html'}
        self.assertEqual(record_from_binding(no_doi, 'colt', 2025)['url'], no_doi['document']['value'])

    def test_publisher_abstract_parsing_is_conservative(self):
        html = '<h1>Paper</h1><div class="abstract"><p>We study learning for protein design.</p></div>'
        self.assertEqual(parse_publisher_abstract(html), 'We study learning for protein design.')
        self.assertIsNone(parse_publisher_abstract('<html><meta name="description" content="Subscribe to our journal."></html>'))

    @patch('conference_meta.request_get')
    def test_publisher_fallback_never_reads_a_pdf_body(self, get):
        self.assertIsNone(publisher_abstract('https://proceedings.mlr.press/example.pdf'))
        get.assert_not_called()
        response = get.return_value.__enter__.return_value
        response.headers = {'Content-Type': 'application/pdf'}
        response.url = 'https://proceedings.mlr.press/example.pdf'
        self.assertIsNone(publisher_abstract('https://doi.org/10.1234/example'))
        self.assertTrue(get.call_args.kwargs['stream'])
        response.iter_content.assert_not_called()

    def test_short_paper_remains_in_all_records_but_not_ai4s(self):
        row = record_from_binding(binding(title='Protein design (Extended Abstract).'), 'ijcai', 2025)
        self.assertEqual(row['ccf_paper_status'], 'excluded')
        self.assertEqual(select_ai4s([row]), [])

    @patch('conference_meta.PAGE_SIZE', 2)
    @patch('conference_meta.crossref_abstract', return_value='Deep learning for protein design.')
    @patch('conference_meta.get_json')
    def test_pagination_dedup_cache_and_limit(self, get_json, abstract):
        one = binding(); two = binding('Second25'); two['doi']['value'] = 'https://doi.org/10.24963/ijcai.2025/2'
        get_json.side_effect = [response([one, two]), response([one, two]), response([])]
        saved = []
        rows = crawl_conference('ijcai', 2025, None, {}, saved.append)
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(saved), 2)
        self.assertIn('OFFSET 2', get_json.call_args_list[2].kwargs['params']['query'])
        self.assertTrue(all(row['abstract'] for row in rows))
        abstract.reset_mock(); get_json.side_effect = [response([one]), response([one])]
        cached = rows[0]
        self.assertEqual(crawl_conference('ijcai', 2025, 1, {cached['id']: cached}, saved.append), [cached])
        abstract.assert_not_called()

    @patch('conference_meta.PAGE_SIZE', 1)
    @patch('conference_meta.publisher_abstract', return_value=None)
    @patch('conference_meta.crossref_abstract', return_value=None)
    @patch('conference_meta.get_json')
    def test_api_failure_keeps_delivered_records_and_repeated_page_fails(self, get_json, abstract, publisher):
        get_json.side_effect = [response([binding()]), response([binding()]), RuntimeError('API failed')]
        saved = []
        with self.assertRaisesRegex(RuntimeError, 'API failed'):
            crawl_conference('ijcai', 2025, None, {}, saved.append)
        self.assertEqual(len(saved), 1)
        get_json.side_effect = [response([binding()]), response([binding()]), response([binding()])]
        with self.assertRaisesRegex(RuntimeError, '重复'):
            crawl_conference('ijcai', 2025, None, {}, saved.append)

    @patch('conference_meta.PAGE_SIZE', 2)
    @patch('conference_meta.publisher_abstract', return_value=None)
    @patch('conference_meta.crossref_abstract', return_value=None)
    @patch('conference_meta.get_json')
    def test_duplicate_doi_across_dblp_records_is_saved_once(self, get_json, abstract, publisher):
        one, duplicate = binding(), binding('Alias25')
        get_json.side_effect = [response([one, duplicate]), response([one, duplicate]), response([])]
        saved = []
        rows = crawl_conference('ijcai', 2025, None, {}, saved.append)
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(saved), 1)

    def test_new_and_old_conference_routing(self):
        with patch('academic.crawl_conference', return_value=[]) as generic:
            academic._crawl_one_metadata('MICCAI', 2025, 1, {}, lambda row: None)
            self.assertEqual(generic.call_args.args[:2], ('miccai', 2025))
        with patch('academic.crawl_kdd', return_value=[]) as kdd:
            academic._crawl_one_metadata('sigkdd', 2025, 1, {}, lambda row: None)
            kdd.assert_called_once()
        self.assertIn('ccf-ab', academic.known_venues())

    def test_cli_expands_all_ccf_and_nature_groups_without_pdf_calls(self):
        argv = ['academic.py', '-v', 'ccf-ab,nature-core', '-y', '2025', '--metadata-only']
        with patch('sys.argv', argv), patch('academic.crawl_metadata_venue', return_value=[]) as crawl, \
                patch('academic.write_merged'), patch('academic.write_run_status'), patch('academic.crawl_venue') as pdf:
            academic.main()
        self.assertEqual(crawl.call_count, 198)
        self.assertEqual(len({call.args[0] for call in crawl.call_args_list}), 198)
        pdf.assert_not_called()


if __name__ == '__main__':
    unittest.main()
