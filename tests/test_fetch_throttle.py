import unittest
from unittest.mock import Mock, patch

import requests
import fetch_util


def response(status, retry_after=None):
    result = Mock(status_code=status, headers={})
    if retry_after:
        result.headers['Retry-After'] = retry_after
    if status >= 400:
        result.raise_for_status.side_effect = requests.HTTPError(response=result)
    else:
        result.raise_for_status.return_value = None
        result.json.return_value = {'ok': True}
    return result


class FetchThrottleTests(unittest.TestCase):
    def test_openalex_budget_cooldown_does_not_block_another_key(self):
        limit = response(429, '3600')
        limit.headers['X-RateLimit-Remaining'] = '0'
        url = 'https://api.openalex.org/works'
        first = {'Authorization': 'Bearer first'}
        second = {'Authorization': 'Bearer second'}
        with patch.dict(fetch_util._NEXT_ALLOWED, {}, clear=True), \
                patch('fetch_util._COOLDOWN_DIR', None), \
                patch('fetch_util._session_get', side_effect=[limit, response(200)]) as get, \
                patch('fetch_util.time.sleep'):
            with self.assertRaises(fetch_util.HostCooldown):
                fetch_util.request_get(url, headers=first)
            with self.assertRaises(fetch_util.HostCooldown):
                fetch_util.request_get(url, headers=first)
            self.assertEqual(fetch_util.request_get(url, headers=second).status_code, 200)
            self.assertEqual(get.call_count, 2)

    def test_openalex_service_outage_still_pauses_both_keys(self):
        url = 'https://api.openalex.org/works'
        with patch.dict(fetch_util._NEXT_ALLOWED, {}, clear=True), \
                patch('fetch_util._COOLDOWN_DIR', None), \
                patch('fetch_util._session_get', return_value=response(503, '120')) as get:
            for key in ('first', 'second'):
                with self.assertRaises(fetch_util.HostCooldown):
                    fetch_util.request_get(url, headers={'Authorization': 'Bearer ' + key})
            get.assert_called_once()

    def test_crossref_rate_limit_uses_bounded_exponential_backoff(self):
        with patch('fetch_util.get_response', side_effect=[
                requests.HTTPError(response=response(429)),
                requests.HTTPError(response=response(429)), response(200)]), \
                patch('fetch_util.time.sleep') as sleep:
            self.assertEqual(fetch_util.get_json('https://api.crossref.org/works'), {'ok': True})
            self.assertEqual([call.args[0] for call in sleep.call_args_list], [15, 30])

    def test_json_retries_rate_limit_but_not_forbidden(self):
        with patch('fetch_util._session_get', side_effect=[response(429, '7'), response(200)]) as get, \
                patch('fetch_util.time.sleep'), patch('fetch_util.time.monotonic', return_value=100):
            self.assertEqual(fetch_util.get_json('https://api.openalex.org/works', retries=2, sleep_s=0), {'ok': True})
            self.assertEqual(get.call_count, 2)
        with patch('fetch_util._session_get', return_value=response(403)) as get, \
                patch('fetch_util.time.sleep'):
            with self.assertRaises(requests.HTTPError):
                fetch_util.get_json('https://example.org', retries=3)
            get.assert_called_once()

    def test_retry_after_cools_down_same_host_without_blocking_other_hosts(self):
        with patch.dict(fetch_util._NEXT_ALLOWED, {}, clear=True), \
                patch('fetch_util._session_get', side_effect=[response(429, '7'), response(200), response(200)]), \
                patch('fetch_util.time.monotonic', return_value=100), patch('fetch_util.time.sleep') as sleep:
            with self.assertRaises(requests.HTTPError):
                fetch_util.get_response('https://api.crossref.org/works/a', retries=1, sleep_s=0)
            fetch_util.get_response('https://sparql.dblp.org/sparql', retries=1, sleep_s=0)
            sleep.assert_not_called()
            fetch_util.get_response('https://api.crossref.org/works/b', retries=1, sleep_s=0)
            sleep.assert_called_once_with(7)


if __name__ == '__main__':
    unittest.main()
