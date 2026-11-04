import unittest
from unittest.mock import Mock, patch

from abstract_sources import fill_abstracts, pubmed_abstracts


class AlternateSourcesTest(unittest.TestCase):
    @patch('abstract_sources.get_text')
    @patch('abstract_sources.get_json', return_value={'esearchresult': {'idlist': ['123']}})
    def test_pubmed_uses_exact_doi_and_keeps_abstract_sections(self, search, fetch):
        fetch.return_value = '''<PubmedArticleSet><PubmedArticle><MedlineCitation><Article>
        <Abstract><AbstractText Label="METHODS">A <i>nested</i> section.</AbstractText></Abstract>
        </Article></MedlineCitation><PubmedData><ArticleIdList>
        <ArticleId IdType="doi">10.1234/ABC</ArticleId>
        </ArticleIdList></PubmedData></PubmedArticle></PubmedArticleSet>'''
        self.assertEqual(pubmed_abstracts(['10.1234/abc']), {'10.1234/abc': 'METHODS: A nested section.'})
        self.assertEqual(pubmed_abstracts(['10.1234/other']), {})

    def test_secondary_sources_only_receive_unresolved_dois(self):
        europe = Mock(return_value={'10.1/b': 'Europe PMC abstract'})
        openaire = Mock(return_value={})
        semantic = Mock(return_value={'10.1/c': 'Semantic Scholar abstract'})
        with patch('abstract_sources.pubmed_abstracts', return_value={}), patch(
            'abstract_sources.europe_pmc_abstracts', europe
        ), patch(
            'abstract_sources.openaire_abstracts', openaire
        ), patch(
            'abstract_sources.semantic_scholar_abstracts', semantic
        ):
            results = fill_abstracts(
                ['10.1/A', '10.1/b', '10.1/c'],
                Mock(return_value={'10.1/a': 'OpenAlex abstract'}),
            )
        europe.assert_called_once_with(['10.1/b', '10.1/c'])
        openaire.assert_not_called()
        semantic.assert_called_once_with(['10.1/c'])
        self.assertEqual(results['10.1/b'], ('Europe PMC abstract', 'europepmc.org'))
        self.assertEqual(results['10.1/c'], ('Semantic Scholar abstract', 'semanticscholar.org'))

    def test_mlsys_uses_official_proceedings(self):
        from academic import _crawl_one_metadata

        with patch('mlsys_meta.crawl_mlsys', return_value=[{'id': 'official'}]) as crawl:
            callback = Mock()
            self.assertEqual(_crawl_one_metadata('mlsys', 2024, 1, {}, callback),
                             [{'id': 'official'}])
            crawl.assert_called_once_with(2024, 1, {}, callback)

    def test_rss_uses_official_proceedings(self):
        from academic import _crawl_one_metadata

        with patch('rss_meta.crawl_rss', return_value=[{'id': 'official'}]) as crawl:
            callback = Mock()
            self.assertEqual(_crawl_one_metadata('rss', 2024, 1, {}, callback),
                             [{'id': 'official'}])
            crawl.assert_called_once_with(1, {}, callback)
