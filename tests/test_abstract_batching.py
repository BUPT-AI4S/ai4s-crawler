import os
import unittest
from unittest.mock import MagicMock, patch

import fetch_util
import kdd_meta


def _dois(count: int) -> list[str]:
    return [f"10.1234/test.{index}" for index in range(count)]


class OpenAlexBatchingTest(unittest.TestCase):
    def test_uses_ninety_doi_batches(self):
        calls = []

        def fake_get_json(url, **kwargs):
            filter_value = kwargs["params"]["filter"].split("doi:", 1)[1]
            dois = filter_value.split("|")
            calls.append((len(dois), kwargs["params"]["per-page"]))
            return {
                "results": [
                    {"doi": f"https://doi.org/{doi}", "abstract_inverted_index": {"word": [0]}}
                    for doi in dois
                ]
            }

        with patch.object(kdd_meta, "get_json", side_effect=fake_get_json):
            found = kdd_meta.openalex_abstracts(_dois(200))

        self.assertEqual(len(calls), 3)
        self.assertEqual([size for size, _ in calls], [90, 90, 20])
        self.assertTrue(all(per_page <= 90 for _, per_page in calls))
        self.assertEqual(len(found), 200)

    def test_splits_failed_batch_in_half(self):
        sizes = []

        def fake_get_json(url, **kwargs):
            size = len(kwargs["params"]["filter"].split("doi:", 1)[1].split("|"))
            sizes.append(size)
            if size > 45:
                raise fetch_util.requests.HTTPError(response=MagicMock(status_code=400))
            return {"results": []}

        with patch.object(kdd_meta, "get_json", side_effect=fake_get_json):
            kdd_meta.openalex_abstracts(_dois(90))

        self.assertEqual(sizes[0], 90)
        self.assertTrue(all(size <= 45 for size in sizes[1:]))


class SemanticScholarBatchingTest(unittest.TestCase):
    def _fake_post(self, calls, status_code=200):
        def fake_post(url, **kwargs):
            calls.append(kwargs)
            response = MagicMock()
            response.status_code = status_code
            response.raise_for_status.return_value = None
            response.json.return_value = [
                {"externalIds": {"DOI": item.split("DOI:", 1)[1]}, "abstract": "a b c"}
                for item in kwargs["json"]["ids"]
            ]
            return response

        return fake_post

    def test_keyed_batches_use_five_hundred(self):
        calls = []
        with patch.dict(os.environ, {"SEMANTIC_SCHOLAR_API_KEY": "secret"}, clear=False):
            with patch("fetch_util.request_post", side_effect=self._fake_post(calls)):
                found = kdd_meta.semantic_scholar_abstracts(_dois(1000))

        self.assertEqual([len(call["json"]["ids"]) for call in calls], [500, 500])
        self.assertTrue(all(call["headers"].get("x-api-key") == "secret" for call in calls))
        self.assertEqual(len(found), 1000)

    def test_anonymous_requests_are_skipped(self):
        calls = []
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("SEMANTIC_SCHOLAR_API_KEY", None)
            os.environ.pop("S2_API_KEY", None)
            with patch("fetch_util.request_post", side_effect=self._fake_post(calls)):
                self.assertEqual(kdd_meta.semantic_scholar_abstracts(_dois(100)), {})

        self.assertEqual(calls, [])


class CrossrefPolitenessTest(unittest.TestCase):
    def test_mailto_param_is_injected(self):
        captured = {}

        def fake_send(url, **kwargs):
            captured.update(kwargs)
            response = MagicMock()
            response.status_code = 200
            response.url = url
            return response

        with patch.object(fetch_util, "_session_get", side_effect=fake_send):
            fetch_util.request_get("https://api.crossref.org/works/10.1234/test.1", params={"select": "DOI"})

        self.assertEqual(captured["params"]["mailto"], fetch_util._CROSSREF_MAILTO)
        self.assertEqual(captured["params"]["select"], "DOI")

    def test_explicit_mailto_is_kept(self):
        captured = {}

        def fake_send(url, **kwargs):
            captured.update(kwargs)
            response = MagicMock()
            response.status_code = 200
            response.url = url
            return response

        with patch.object(fetch_util, "_session_get", side_effect=fake_send):
            fetch_util.request_get("https://api.crossref.org/works/10.1234/test.1", params={"mailto": "someone@example.org"})

        self.assertEqual(captured["params"]["mailto"], "someone@example.org")


if __name__ == "__main__":
    unittest.main()
