import unittest
from unittest.mock import MagicMock, patch
import requests
from conference_meta import publisher_abstract


class PublisherRetryTests(unittest.TestCase):
    def test_connection_failure_retries_once_and_keeps_real_abstract(self):
        response = MagicMock()
        body = response.__enter__.return_value
        body.headers = {'Content-Type': 'text/html'}
        body.encoding = 'utf-8'
        body.iter_content.return_value = [b'<div class="acl-abstract">Real paper abstract.</div>']
        with patch('conference_meta.request_get', side_effect=[requests.ConnectionError('closed'), response]) as get, \
                patch('conference_meta.time.sleep'):
            self.assertEqual(publisher_abstract('https://aclanthology.org/2024.lrec-main.1/'), 'Real paper abstract.')
        self.assertEqual(get.call_count, 2)

    def test_retries_are_bounded_and_forbidden_is_not_retried(self):
        with patch('conference_meta.request_get', side_effect=requests.ConnectionError('closed')) as get, \
                patch('conference_meta.time.sleep'):
            with self.assertRaises(requests.ConnectionError):
                publisher_abstract('https://aclanthology.org/2024.lrec-main.1/')
        self.assertEqual(get.call_count, 2)
        response = MagicMock()
        response.__enter__.return_value.raise_for_status.side_effect = requests.HTTPError(response=MagicMock(status_code=403))
        with patch('conference_meta.request_get', return_value=response) as get:
            with self.assertRaises(requests.HTTPError):
                publisher_abstract('https://aclanthology.org/2024.lrec-main.1/')
        get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
