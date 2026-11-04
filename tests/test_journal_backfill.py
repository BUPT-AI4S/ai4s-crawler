import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import requests

import journal_meta
from journal_abstract_backfill import backfill_journal_abstracts, _parallel_openalex
from paper_record import dump_records, load_records


class JournalBackfillTest(unittest.TestCase):
    def test_biomedical_pass_saves_first_provider_before_second(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root = Path(tmp)
            path = root / 'a/2024/papers.json'
            dump_records(path, [{'id': 'a', 'doi': '10.1/a', 'title': 'Paper A'},
                                {'id': 'b', 'doi': '10.1/b', 'title': 'Paper B'}])

            def pubmed(dois):
                self.assertEqual(dois, ['10.1/b'])
                self.assertEqual(load_records(path)[0]['abstract'], 'Abstract A')
                return {'10.1/b': 'Abstract B'}

            with patch('journal_abstract_backfill.europe_pmc_abstracts',
                       return_value={'10.1/a': 'Abstract A'}), \
                    patch('journal_abstract_backfill.pubmed_abstracts', side_effect=pubmed), \
                    patch('journal_abstract_backfill.openalex_abstracts') as openalex:
                backfill_journal_abstracts(root, 2024, ['a'], biomedical_only=True)
            openalex.assert_not_called()
            self.assertEqual([row['abstract'] for row in load_records(path)], ['Abstract A', 'Abstract B'])

    def test_openalex_only_leaves_unmatched_records_for_later(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root = Path(tmp)
            path = root / 'a/2024/papers.json'
            dump_records(path, [{'id': 'a', 'doi': '10.1/a', 'title': 'Paper A'},
                                {'id': 'b', 'doi': '10.1/b', 'title': 'Paper B'}])
            with patch('journal_abstract_backfill.openalex_abstracts', return_value={'10.1/a': 'Abstract A'}), \
                    patch('journal_abstract_backfill.fill_abstracts') as fallback, \
                    patch('journal_abstract_backfill.publisher_details') as publisher:
                backfill_journal_abstracts(root, 2024, ['a'], openalex_only=True)
            fallback.assert_not_called()
            publisher.assert_not_called()
            self.assertEqual([row.get('abstract') for row in load_records(path)], ['Abstract A', None])

    def test_openalex_hit_is_on_disk_before_slow_fallback(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root = Path(tmp)
            path = root / 'a/2024/papers.json'
            dump_records(path, [
                {'id': 'a', 'doi': '10.1/a', 'title': 'Paper A'},
                {'id': 'b', 'doi': '10.1/b', 'title': 'Paper B'},
            ])

            def fallback(dois, lookup, **kwargs):
                hits = lookup(dois)
                self.assertEqual(load_records(path)[0].get('abstract'), 'Abstract A')
                self.assertIsNone(load_records(path)[1].get('abstract'))
                return {doi: (abstract, 'openalex.org') for doi, abstract in hits.items()}

            with patch('journal_abstract_backfill.openalex_abstracts', return_value={'10.1/a': 'Abstract A'}), \
                    patch('journal_abstract_backfill.fill_abstracts', side_effect=fallback), \
                    patch('journal_abstract_backfill.publisher_details', return_value={}):
                backfill_journal_abstracts(root, 2024, ['a'])

    def test_openalex_batches_are_bounded(self):
        with patch('journal_abstract_backfill.openalex_abstracts',
                   side_effect=lambda dois: {doi: 'abstract' for doi in dois}) as lookup:
            dois = [f'10.1/{i}' for i in range(201)]
            self.assertEqual(set(_parallel_openalex(dois)), set(dois))
        self.assertEqual(sorted(len(c.args[0]) for c in lookup.call_args_list), [21, 90, 90])

    def test_duplicate_doi_is_batched_and_success_is_reused_on_next_pass(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root = Path(tmp)
            for folder in ('a', 'b', 'c'):
                dump_records(root / folder / '2024' / 'papers.json', [
                    {'id': '10.1/example', 'doi': '10.1/example',
                     'title': 'Example paper', 'article_type': 'Article'},
                ])
            with patch('journal_abstract_backfill.fill_abstracts', side_effect=[
                {'10.1/example': ('Published abstract', 'openalex.org')}, {},
            ]) as fill:
                backfill_journal_abstracts(root, 2024, ['a', 'b'])
                backfill_journal_abstracts(root, 2024, ['c'])
            self.assertEqual([call.args[0] for call in fill.call_args_list], [['10.1/example']])
            for folder in ('a', 'b', 'c'):
                dest = root / folder / '2024'
                row = load_records(dest / 'papers.json')[0]
                self.assertEqual(row['abstract'], 'Published abstract')
                self.assertEqual(row['screening_status'], 'ready')
                self.assertTrue((dest / 'ai4s.json').exists())

    def test_failed_publisher_is_skipped_during_cooldown(self):
        with patch.dict(journal_meta._PUBLISHER_RETRY_AT, {}, clear=True), patch(
            'journal_meta._read_publisher_details', side_effect=requests.ConnectionError
        ) as read:
            with self.assertRaises(requests.ConnectionError):
                journal_meta.publisher_details('https://example.org/paper1')
            self.assertEqual(journal_meta.publisher_details('https://example.org/paper2'), {})
            read.assert_called_once()
