import unittest
from unittest.mock import patch
import requests

from nature_meta import crawl_nature, parse_article_page, record_from_crossref
from nature_journals import JOURNALS, expand_venues, parse_issn, resolve_issn


def work(doi='10.1038/example', abstract=None):
    return {'DOI': doi, 'title': ['Deep learning for protein design'],
            'author': [{'given': 'A', 'family': 'Li', 'ORCID': 'https://orcid.org/1'}],
            'published-online': {'date-parts': [[2025, 5, 2]]},
            'published-print': {'date-parts': [[2026, 1]]},
            'abstract': abstract, 'subject': ['Biology'], 'type': 'journal-article'}


class NatureTests(unittest.TestCase):
    @patch('nature_meta.resolve_issn')
    @patch('nature_meta.get_json', return_value={'message': {'items': []}})
    def test_historical_journal_uses_its_2024_issn(self, fetch, resolve):
        crawl_nature('npjheritagesci', 2024, None, {}, lambda row: None)
        resolve.assert_not_called()
        self.assertIn('/2050-7445/works', fetch.call_args.args[0])

    @patch('nature_meta.resolve_issn', return_value='3091-5244')
    @patch('nature_meta.get_json')
    def test_missing_journal_index_falls_back_to_issn_search(self, fetch, issn):
        response = requests.Response()
        response.status_code = 404
        fetch.side_effect = [requests.HTTPError(response=response),
                             {'message': {'items': [], 'total-results': 0}}]
        self.assertEqual(crawl_nature('natmecheng', 2024, None, {}, lambda row: None), [])
        call = fetch.call_args_list[1]
        self.assertEqual(call.args[0], 'https://api.crossref.org/works')
        self.assertIn('issn:3091-5244', call.kwargs['params']['filter'])
        self.assertIn('from-pub-date:2024-01-01', call.kwargs['params']['filter'])
        self.assertEqual(call.kwargs['params']['cursor'], '*')

    @patch('nature_meta.resolve_issn', return_value='3091-5244')
    @patch('nature_meta.get_json')
    def test_access_errors_are_not_treated_as_empty_journals(self, fetch, issn):
        response = requests.Response()
        response.status_code = 403
        fetch.side_effect = requests.HTTPError(response=response)
        with self.assertRaises(requests.HTTPError):
            crawl_nature('natmecheng', 2024, None, {}, lambda row: None)
        self.assertEqual(fetch.call_count, 1)

    def test_custom_openreview_venue_is_case_sensitive(self):
        venue = 'ICLR.cc/2025/Conference'
        self.assertEqual(expand_venues([venue]), [venue])

    def test_registry_and_aliases(self):
        self.assertEqual(expand_venues(['ncs', 'natcomputsci', 'nmi']), ['natcomputsci', 'natmachintell'])
        for key in ['nature', 'ncomms', 'nmeth', 'sdata', 'srep', 'npjcompumats', 'npjdigitalmed', 'commschem']:
            self.assertIn(key, JOURNALS)
        self.assertGreater(len(expand_venues(['nature-npj'])), 30)
        self.assertNotIn('natafrica', JOURNALS)

    def test_issn_from_meta_or_footer_and_invalid_page(self):
        self.assertEqual(parse_issn('<meta name="prism.issn" content="2662-8457">'), '2662-8457')
        self.assertEqual(parse_issn('<p>ISSN 1476-4687 (online)</p>'), '1476-4687')
        with self.assertRaises(ValueError):
            parse_issn('<html>Access denied</html>')

    @patch('nature_journals.get_text', return_value='<meta name="prism.issn" content="2052-4463">')
    def test_scientific_data_issn_uses_homepage(self, fetch):
        resolve_issn.cache_clear()
        self.assertEqual(resolve_issn('sdata'), '2052-4463')
        fetch.assert_called_once_with('https://www.nature.com/sdata/')
        resolve_issn.cache_clear()

    def test_record_prefers_online_date_and_strips_jats(self):
        row = record_from_crossref(work(abstract='<jats:p>Protein <jats:italic>design</jats:italic>.</jats:p>'), 'natcomputsci', 2025, '2662-8457')
        self.assertEqual(row['published'], '2025-05-02')
        self.assertEqual(row['abstract'], 'Protein design .')
        self.assertEqual(row['venue_type'], 'journal')
        self.assertEqual(row['doi'], '10.1038/example')
        self.assertEqual(row['id'], '10.1038/example')
        self.assertEqual(row['journal_title'], 'Nature Computational Science')
        self.assertIsNone(row['pdf_url'])

    def test_article_page_extracts_abstract_type_keywords(self):
        html = '''<meta name="dc.type" content="OriginalPaper">
        <meta name="citation_article_type" content="Article">
        <meta name="citation_pdf_url" content="https://www.nature.com/articles/example.pdf">
        <section data-title="Abstract"><h2>Abstract</h2><div class="c-article-section__content"><p>We use deep learning for proteins.</p></div></section>
        <meta name="dc.subject" content="Protein design">'''
        detail = parse_article_page(html)
        self.assertEqual(detail['abstract'], 'We use deep learning for proteins.')
        self.assertEqual(detail['article_type'], 'Article')
        self.assertEqual(detail['keywords'], ['Protein design'])

    def test_brief_communications_are_research_not_commentary(self):
        from ai4s_filter import select_ai4s
        rows = select_ai4s([{'title': 'Neural networks for protein design', 'venue_type': 'journal',
                            'article_type': 'Brief Communication'}])
        self.assertEqual(len(rows), 1)

    @patch('nature_meta.get_text', return_value='<meta name="citation_article_type" content="Article">')
    @patch('nature_meta.get_json')
    @patch('nature_meta.resolve_issn', return_value='2662-8457')
    def test_cursor_pagination_dedup_and_resume(self, issn, get_json, get_text):
        first = work(abstract='A neural network for protein design')
        second = work('10.1038/second', 'Molecular machine learning')
        get_json.side_effect = [
            {'message': {'items': [first], 'next-cursor': 'page2', 'total-results': 2}},
            {'message': {'items': [first, second], 'next-cursor': 'page3'}},
            {'message': {'items': []}},
        ]
        saved = []
        rows = crawl_nature('natcomputsci', 2025, None, {}, saved.append)
        self.assertEqual(len(rows), 2)
        self.assertEqual(len(saved), 2)
        self.assertEqual(get_json.call_args_list[1].kwargs['params']['cursor'], 'page2')
        self.assertNotIn('sort', get_json.call_args_list[0].kwargs['params'])
        cached = dict(rows[0], abstract='cached abstract', article_type='Article')
        get_json.side_effect = [{'message': {'items': [first]}}]
        get_text.reset_mock()
        self.assertEqual(crawl_nature('natcomputsci', 2025, 1, {cached['id']: cached}, saved.append)[0]['abstract'], 'cached abstract')
        get_text.assert_not_called()

    @patch('nature_meta.get_text', return_value='<meta name="citation_article_type" content="Article">')
    @patch('nature_meta.get_json')
    @patch('nature_meta.resolve_issn', return_value='2662-8457')
    def test_limit_and_failure_checkpoint(self, issn, get_json, detail):
        get_json.return_value = {'message': {'items': [work(), work('10.1038/second')]}}
        saved = []
        self.assertEqual(len(crawl_nature('natcomputsci', 2025, 1, {}, saved.append)), 1)
        self.assertEqual(len(saved), 1)
        get_json.side_effect = [{'message': {'items': [work()], 'next-cursor': 'next'}}, RuntimeError('API failed')]
        with self.assertRaisesRegex(RuntimeError, 'API failed'):
            crawl_nature('natcomputsci', 2025, None, {}, saved.append)
        self.assertEqual(saved[-1]['doi'], '10.1038/example')


if __name__ == '__main__':
    unittest.main()
