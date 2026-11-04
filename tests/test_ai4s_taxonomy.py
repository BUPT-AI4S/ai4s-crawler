import unittest

from ai4s_filter import select_ai4s
from ai4s_taxonomy import CATEGORIES, classify_paper


class TaxonomyTests(unittest.TestCase):
    def test_expanded_discipline_topics(self):
        cases = [
            ('Equivariant neural networks for interatomic potentials', 'AI for 物质科学', 'interatomic potential'),
            ('Deep learning for retrosynthetic planning', 'AI for 物质科学', 'retrosynthesis'),
            ('Graph neural networks for ADMET prediction', 'AI for 生命科学', 'ADMET prediction'),
            ('Machine learning for spatial transcriptomics', 'AI for 生命科学', 'spatial transcriptomics'),
            ('Deep learning for enzyme engineering', 'AI for 生命科学', 'enzyme engineering'),
            ('Machine learning for numerical integration of stochastic differential equations', 'AI for 数理科学', 'stochastic differential equation'),
            ('Neural networks for turbulence closure', 'AI for 数理科学', 'turbulence modelling'),
            ('Deep learning for gravitational wave detection', 'AI for 地球宇宙科学', 'gravitational waves'),
            ('Graph neural networks for precipitation nowcasting', 'AI for 地球宇宙科学', 'precipitation nowcasting'),
            ('Machine learning for seismic inversion', 'AI for 地球宇宙科学', 'seismic inversion'),
            ('Deep learning for channel estimation in wireless communications', 'AI for 信息科学', 'channel estimation'),
            ('Graph neural networks for electronic design automation', 'AI for 信息科学', 'electronic design automation'),
            ('Machine learning for causal inference in public policy', 'AI for 社会科学', 'public policy'),
            ('Deep learning for human mobility prediction', 'AI for 社会科学', 'human mobility'),
        ]
        for title, category, keyword in cases:
            with self.subTest(title=title):
                rows = select_ai4s([{'title': title, 'venue_type': 'journal', 'article_type': 'Article'}])
                self.assertEqual(len(rows), 1)
                self.assertIn(category, rows[0]['ai4s_tags'])
                self.assertIn(keyword, rows[0]['ai4s_keywords'])

    def test_expanded_capabilities(self):
        for title, category, keyword in [
            ('A single-cell atlas for machine learning', '科学数据', 'scientific atlas'),
            ('A neural emulator for climate models', '科学知识模型', 'surrogate model'),
            ('A genomic language model pretrained with masked language modeling', '科学基础模型', 'genomic language model'),
            ('An AI scientist for automated scientific discovery', '科学智能体', 'AI scientist'),
            ('A protein out-of-distribution generalization benchmark', '科学评测', 'out-of-distribution evaluation'),
            ('Closed-loop robotic synthesis of catalysts', '自主实验室', 'robotic synthesis'),
        ]:
            with self.subTest(title=title):
                row = classify_paper({'title': title})
                self.assertIn(category, row['ai4s_tags'])
                self.assertIn(keyword, row['ai4s_keywords'])

    def test_method_synonyms_unicode_hyphens_and_word_boundaries(self):
        paper = {'title': 'Self–supervised pre–training of protein language models using GNNs'}
        row = classify_paper(paper)
        for term in ['self-supervised learning', 'pretraining', 'graph neural network', 'protein language model']:
            self.assertIn(term, row['ai4s_keywords'])
        self.assertIn('科学基础模型', row['ai4s_tags'])
        for title in ['GNNs for node classification', 'A transformer for sentiment analysis',
                      'An atlas benchmark for image classification', 'An SDEdit image model',
                      'Rainbows in decorative designs']:
            with self.subTest(title=title):
                self.assertEqual(classify_paper({'title': title})['ai4s_tags'], [])
                self.assertEqual(classify_paper({'title': title})['ai4s_keywords'], [])

    def test_chinese_scientific_terms(self):
        row = select_ai4s([{'title': '基于图神经网络的电池材料发现与分子设计', 'venue_type': 'journal'}])
        self.assertEqual(len(row), 1)
        for keyword in ['graph neural network', 'materials', 'molecular design', 'battery']:
            self.assertIn(keyword, row[0]['ai4s_keywords'])

    def test_phrases_do_not_span_metadata_fields(self):
        row = classify_paper({'title': 'A novel protein', 'abstract': 'Language models are useful tools.'})
        self.assertNotIn('protein language model', row['ai4s_keywords'])

    def test_metaphorical_catalyst_is_not_chemistry(self):
        paper = {'title': 'Dataset Ownership Verification in Contrastive Pre-trained Models',
                 'abstract': 'High-quality datasets have become the primary catalyst for the swift progress of deep learning.'}
        self.assertEqual(classify_paper(paper)['ai4s_tags'], [])
        self.assertEqual(select_ai4s([paper]), [])
        real = {'title': 'Machine learning for catalysts for hydrogen production'}
        self.assertIn('AI for 物质科学', classify_paper(real)['ai4s_tags'])

    def test_explicit_chinese_scientific_categories(self):
        for title, category in [
            ('科学数据集的整理与发布', '科学数据'),
            ('用于科学发现的科学智能体', '科学智能体'),
            ('科学推理评测基准', '科学评测'),
            ('科学知识模型的方法研究', '科学知识模型'),
            ('用于天气预报的神经算子', 'AI for 地球宇宙科学'),
        ]:
            with self.subTest(title=title):
                self.assertIn(category, classify_paper({'title': title})['ai4s_tags'])

    def test_exact_screenshot_categories(self):
        self.assertEqual(set(CATEGORIES), {
            '科学数据', '科学知识模型', '科学基础模型', '科学智能体', '科学评测', '自主实验室',
            'AI for 数理科学', 'AI for 生命科学', 'AI for 物质科学',
            'AI for 地球宇宙科学', 'AI for 信息科学', 'AI for 社会科学',
        })

    def test_multilabel_and_fine_keywords_without_changing_author_keywords(self):
        paper = {'title': 'A protein foundation model for molecular design', 'keywords': ['author term']}
        result = classify_paper(paper)
        self.assertIn('科学基础模型', result['ai4s_tags'])
        self.assertIn('AI for 生命科学', result['ai4s_tags'])
        self.assertIn('AI for 物质科学', result['ai4s_tags'])
        self.assertIn('protein', result['ai4s_keywords'])
        self.assertEqual(paper['keywords'], ['author term'])

    def test_scientific_dataset_is_not_any_ml_dataset(self):
        self.assertNotIn('科学数据', classify_paper({'title': 'A dataset for image classification'})['ai4s_tags'])
        self.assertIn('科学数据', classify_paper({'title': 'A protein structure dataset'})['ai4s_tags'])

    def test_using_a_dataset_is_not_a_data_contribution(self):
        paper = {'title': 'Deep learning for protein design',
                 'abstract': 'We train our model on three datasets and compare results.'}
        self.assertNotIn('科学数据', classify_paper(paper)['ai4s_tags'])

    def test_new_domains_and_methods_are_recalled(self):
        for title, tag in [
            ('Deep learning for economic forecasting', 'AI for 社会科学'),
            ('Neural networks for error correcting codes', 'AI for 信息科学'),
            ('Autonomous laboratory for materials discovery', '自主实验室'),
            ('Scientific agent for automated discovery', '科学智能体'),
        ]:
            with self.subTest(title=title):
                rows = select_ai4s([{'title': title}])
                self.assertEqual(len(rows), 1)
                self.assertIn(tag, rows[0]['ai4s_tags'])

    def test_journals_require_ai_evidence_not_only_science_terms(self):
        plain = {'title': 'Protein folding in molecular systems', 'venue_type': 'journal'}
        self.assertEqual(select_ai4s([plain]), [])
        ai = dict(plain, title='Deep learning for protein folding')
        self.assertEqual(len(select_ai4s([ai])), 1)

    def test_generic_ai_is_not_science_and_editorials_are_excluded(self):
        self.assertEqual(select_ai4s([{'title': 'A foundation model for image classification', 'venue_type': 'journal'}]), [])
        self.assertEqual(select_ai4s([{'title': 'Deep learning for protein design', 'venue_type': 'journal', 'article_type': 'Editorial'}]), [])

    def test_research_highlights_and_correspondence_are_not_research_papers(self):
        for article_type in ['Research Highlight', 'Matters Arising', 'Correspondence', 'Book Review']:
            with self.subTest(article_type=article_type):
                self.assertEqual(select_ai4s([{'title': 'Deep learning for protein design',
                                 'venue_type': 'journal', 'article_type': article_type}]), [])

    def test_existing_reviewed_tags_are_preserved(self):
        paper = {'title': 'Protein structure prediction', 'ai4s_tags': ['人工复核标签'],
                 'ai4s_tagging': {'status': 'classified'}, 'ai4s_keywords': ['curated']}
        row = select_ai4s([paper])[0]
        self.assertEqual(row['ai4s_tags'], paper['ai4s_tags'])
        self.assertEqual(row['ai4s_keywords'], ['curated'])
        self.assertNotIn('ai4s_hits', paper)

    def test_materials_imaging_and_bioimage_research_are_recalled(self):
        examples = [
            ('Deep learning for materials image processing and atomistic modelling', 'AI for 物质科学'),
            ('Machine learning for bioimage analysis', 'AI for 生命科学'),
        ]
        for title, tag in examples:
            with self.subTest(title=title):
                rows = select_ai4s([{'title': title, 'venue_type': 'journal', 'article_type': 'Article'}])
                self.assertEqual(len(rows), 1)
                self.assertIn(tag, rows[0]['ai4s_tags'])


if __name__ == '__main__':
    unittest.main()
