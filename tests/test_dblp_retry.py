import unittest
from unittest import mock

import requests

import conference_meta
import academic


def _http_error(status: int) -> requests.HTTPError:
    response = requests.Response()
    response.status_code = status
    return requests.HTTPError(f'{status} error', response=response)


EMPTY_PAYLOAD = {'results': {'bindings': []}}


class PageRetryTests(unittest.TestCase):
    def test_transient_failure_is_retried_then_succeeds(self):
        calls = []

        def fake_get_json(*args, **kwargs):
            calls.append(kwargs)
            if len(calls) < 3:
                raise _http_error(503)
            return EMPTY_PAYLOAD

        with mock.patch.object(conference_meta, 'get_json', fake_get_json), \
                mock.patch.object(conference_meta.time, 'sleep') as sleep, \
                mock.patch.object(conference_meta, 'PAGE_RETRIES', 5), \
                mock.patch.object(conference_meta, 'PAGE_BACKOFF', 1.0):
            payload = conference_meta._page_payload('iros', 2024, 100, 0)

        self.assertEqual(payload, EMPTY_PAYLOAD)
        self.assertEqual(len(calls), 3)
        self.assertEqual(sleep.call_count, 2)
        # 单页内部不再叠加 get_json 自带重试，避免退避时间层层放大。
        self.assertTrue(all(call['retries'] == 1 for call in calls))

    def test_backoff_is_capped(self):
        sleeps = []

        def fake_get_json(*args, **kwargs):
            raise _http_error(503)

        with mock.patch.object(conference_meta, 'get_json', fake_get_json), \
                mock.patch.object(conference_meta.time, 'sleep', sleeps.append), \
                mock.patch.object(conference_meta, 'PAGE_RETRIES', 4), \
                mock.patch.object(conference_meta, 'PAGE_BACKOFF', 10.0):
            with self.assertRaises(requests.HTTPError):
                conference_meta._page_payload('iros', 2024, 100, 0)

        self.assertEqual(sleeps, [10.0, 20.0, 40.0])

    def test_permanent_error_is_not_retried(self):
        calls = []

        def fake_get_json(*args, **kwargs):
            calls.append(1)
            raise _http_error(404)

        with mock.patch.object(conference_meta, 'get_json', fake_get_json), \
                mock.patch.object(conference_meta.time, 'sleep') as sleep:
            with self.assertRaises(requests.HTTPError):
                conference_meta._page_payload('iros', 2024, 100, 0)

        self.assertEqual(len(calls), 1)
        sleep.assert_not_called()


class RetryableSourceTests(unittest.TestCase):
    def test_transient_errors_are_retryable(self):
        for status in (429, 500, 502, 503, 504):
            self.assertTrue(academic._is_retryable_upstream(_http_error(status)))
        self.assertTrue(academic._is_retryable_upstream(requests.Timeout('t')))
        self.assertTrue(academic._is_retryable_upstream(
            academic.HostCooldown('sparql.dblp.org 冷却至 2026-11-05T00:00:01，剩余 3600 秒，保留断点后退出本次来源采集')))

    def test_permanent_errors_are_not_retryable(self):
        self.assertFalse(academic._is_retryable_upstream(_http_error(404)))
        self.assertFalse(academic._is_retryable_upstream(
            RuntimeError('iros: 新增会议书目检索为空，需核对当届论文集，不能认定采集完整')))
        self.assertFalse(academic._is_retryable_upstream(ValueError('bad')))


if __name__ == '__main__':
    unittest.main()
