import unittest
from unittest.mock import Mock, patch

from abstract_sources import OPENAIRE_BATCH, fill_abstracts, openaire_abstracts


def _record(doi, *descriptions):
    return {'metadata': {'oaf:entity': {'oaf:result': {
        'pid': {'@classid': 'doi', '$': doi},
        'description': [{'$': text} for text in descriptions],
    }}}}


class OpenaireSourceTest(unittest.TestCase):
    @patch('abstract_sources.get_json')
    def test_batches_dois_and_unwraps_green_oa_description(self, get_json):
        get_json.return_value = {'response': {'results': {'result': [
            _record('10.1016/J.LANDURBPLAN.2023.104901',
                    '<jats:p>Short abstract.</jats:p>',
                    '<jats:p>Longer abstract with &amp; entity and <jats:italic>markup</jats:italic>.</jats:p>'
                    + ' padding' * 40),
            _record('10.9999/not-requested', '<jats:p>' + 'x' * 400 + '</jats:p>'),
        ]}}}

        found = openaire_abstracts(['10.1016/j.landurbplan.2023.104901'])

        self.assertEqual(list(found), ['10.1016/j.landurbplan.2023.104901'])
        self.assertIn('Longer abstract with & entity and markup', found['10.1016/j.landurbplan.2023.104901'])
        self.assertNotIn('<jats:', found['10.1016/j.landurbplan.2023.104901'])
        params = get_json.call_args.kwargs['params']
        self.assertIn(('format', 'json'), params)
        self.assertIn(('size', '100'), params)
        self.assertEqual([value for key, value in params if key == 'doi'],
                         ['10.1016/j.landurbplan.2023.104901'])

    @patch('abstract_sources.get_json')
    def test_splits_large_requests_by_batch_size(self, get_json):
        get_json.return_value = {'response': {'results': {'result': []}}}
        dois = [f'10.1234/{index}' for index in range(OPENAIRE_BATCH * 2 + 3)]

        self.assertEqual(openaire_abstracts(dois), {})
        self.assertEqual(get_json.call_count, 3)

    @patch('abstract_sources.get_json', side_effect=RuntimeError('boom'))
    def test_failure_keeps_pipeline_alive(self, _get_json):
        self.assertEqual(openaire_abstracts(['10.1234/abc']), {})

    @patch('abstract_sources.get_json')
    def test_oversized_batch_splits_instead_of_aborting(self, get_json):
        sizes = []

        def fake(_url, params=None, **_kwargs):
            dois = [value for key, value in params if key == 'doi']
            sizes.append(len(dois))
            if len(dois) > 25:
                raise RuntimeError('HTTP Error 409: Conflict')
            return {'response': {'results': {'result': []}}}

        get_json.side_effect = fake
        self.assertEqual(openaire_abstracts([f'10.1234/{index}' for index in range(50)]), {})
        self.assertEqual(sizes[:3], [50, 25, 25])

    def test_pipeline_skips_openaire_once_everything_is_resolved(self):
        openaire = Mock(return_value={})
        with patch('abstract_sources.openaire_abstracts', openaire), patch(
            'abstract_sources.pubmed_abstracts', return_value={}
        ), patch('abstract_sources.europe_pmc_abstracts', return_value={}), patch(
            'abstract_sources.semantic_scholar_abstracts', return_value={}
        ):
            results = fill_abstracts(['10.1/a', '10.1/b'],
                                     Mock(return_value={'10.1/a': 'OpenAlex abstract'}),
                                     include_openaire=True)
        openaire.assert_called_once_with(['10.1/b'])
        self.assertEqual(results['10.1/a'], ('OpenAlex abstract', 'openalex.org'))
