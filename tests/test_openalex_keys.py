import unittest
from unittest.mock import Mock, patch

import fetch_util
import kdd_meta


def response(status=200, headers=None):
    result = Mock(status_code=status, headers=headers or {})
    result.raise_for_status.return_value = None
    result.json.return_value = {'results': []}
    return result


class OpenAlexKeyRotationTests(unittest.TestCase):
    def setUp(self):
        kdd_meta._OPENALEX_ROTATION = __import__('itertools').count()

    def test_both_keys_are_collected_without_duplicates(self):
        with patch.dict('os.environ', {'OPENALEX_API_KEY': 'first',
                                       'OPENALEX_PREVIEW_API_KEY': 'second'}, clear=False):
            self.assertEqual(kdd_meta.openalex_keys(), ['first', 'second'])
        with patch.dict('os.environ', {'OPENALEX_API_KEY': 'same',
                                       'OPENALEX_PREVIEW_API_KEY': 'same'}, clear=False):
            self.assertEqual(kdd_meta.openalex_keys(), ['same'])

    def test_rotation_alternates_between_keys(self):
        with patch.dict('os.environ', {'OPENALEX_API_KEY': 'first',
                                       'OPENALEX_PREVIEW_API_KEY': 'second'}, clear=False):
            picked = [kdd_meta.next_openalex_key() for _ in range(4)]
        self.assertEqual(set(picked), {'first', 'second'})
        self.assertNotEqual(picked[0], picked[1])
        self.assertEqual(picked[0], picked[2])

    def test_no_key_returns_none(self):
        with patch.dict('os.environ', {'OPENALEX_API_KEY': '', 'OPENALEX_PREVIEW_API_KEY': ''},
                        clear=False):
            self.assertIsNone(kdd_meta.next_openalex_key())

    @patch('kdd_meta.get_json', return_value={'results': []})
    def test_batches_use_alternating_keys(self, get_json):
        with patch.dict('os.environ', {'OPENALEX_API_KEY': 'first',
                                       'OPENALEX_PREVIEW_API_KEY': 'second'}, clear=False):
            kdd_meta.openalex_abstracts(['10.1/a'])
            kdd_meta.openalex_abstracts(['10.1/b'])
        tokens = [call.kwargs['headers']['Authorization'] for call in get_json.call_args_list]
        self.assertEqual(len(tokens), 2)
        self.assertEqual(set(tokens), {'Bearer first', 'Bearer second'})

    @patch('kdd_meta.get_json', return_value={'results': []})
    def test_explicit_key_still_wins(self, get_json):
        with patch.dict('os.environ', {'OPENALEX_API_KEY': 'first',
                                       'OPENALEX_PREVIEW_API_KEY': 'second'}, clear=False):
            kdd_meta.openalex_abstracts(['10.1/a'], api_key='pinned')
        self.assertEqual(get_json.call_args.kwargs['headers']['Authorization'], 'Bearer pinned')


class OpenAlexPerKeyBudgetTests(unittest.TestCase):
    def test_each_key_gets_its_own_rate_and_slot_budget(self):
        scope = 'api.openalex.org:key:abc123'
        self.assertAlmostEqual(fetch_util._budget_interval(scope, 'api.openalex.org'),
                               1.0 / fetch_util._OPENALEX_KEY_RPS)
        self.assertEqual(fetch_util._budget_slots(scope, 'api.openalex.org'),
                         fetch_util._OPENALEX_KEY_SLOTS)

    def test_keyless_requests_keep_host_budget(self):
        host = 'api.openalex.org'
        self.assertEqual(fetch_util._budget_interval(host, host),
                         fetch_util._HOST_INTERVALS[host])
        self.assertEqual(fetch_util._budget_slots(host, host), fetch_util._HOST_CONCURRENCY[host])

    @patch('fetch_util._session_get', side_effect=[response(), response()])
    def test_two_keys_do_not_share_a_semaphore(self, _get):
        with patch.dict(fetch_util._NEXT_ALLOWED, {}, clear=True), \
                patch.dict(fetch_util._ACCOUNT_COOLDOWNS, {}, clear=True), \
                patch('fetch_util.time.sleep'):
            fetch_util.request_get('https://api.openalex.org/works',
                                   headers={'Authorization': 'Bearer first'})
            fetch_util.request_get('https://api.openalex.org/works',
                                   headers={'Authorization': 'Bearer second'})
        keys = [key for key in fetch_util._HOST_SLOTS if ':key:' in key]
        self.assertEqual(len(keys), 2)


if __name__ == '__main__':
    unittest.main()
