import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import academic


class NatureIntegrationTests(unittest.TestCase):
    def test_limit_cannot_replace_existing_metadata(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as tmp:
            path = Path(tmp) / 'natcomputsci/2025/papers.json'
            path.parent.mkdir(parents=True)
            path.write_text('[{"id": "existing"}]', encoding='utf-8')
            with patch('academic._crawl_one_metadata', return_value=[]), \
                    self.assertRaisesRegex(ValueError, 'metadata-dir'):
                academic.crawl_metadata_venue('ncs', 2025, 1, Path(tmp))
            self.assertEqual(json.loads(path.read_text(encoding='utf-8')), [{'id': 'existing'}])

    def test_alias_routes_to_canonical_journal(self):
        with patch('academic.crawl_nature', return_value=[]) as crawl:
            academic._crawl_one_metadata('ncs', 2025, 1, {}, lambda row: None)
        self.assertEqual(crawl.call_args.args[:2], ('natcomputsci', 2025))
        self.assertEqual(academic._folder_name('NCS'), 'natcomputsci')

    def test_interruption_flushes_tail_checkpoint(self):
        def interrupted(venue, year, limit, existing, on_new, *, flush=None):
            on_new({'id': 'doi:1', 'title': 'Protein structure'})
            raise RuntimeError('network interrupted')

        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as tmp:
            with patch('academic._crawl_one_metadata', side_effect=interrupted):
                with self.assertRaisesRegex(RuntimeError, 'network interrupted'):
                    academic.crawl_metadata_venue('ncs', 2025, None, Path(tmp))
            rows = json.loads((Path(tmp) / 'natcomputsci/2025/papers.json').read_text(encoding='utf-8'))
            self.assertEqual(rows[0]['id'], 'doi:1')

    def test_interruption_also_screens_saved_papers_and_keeps_failure(self):
        row = {'id': 'doi:1', 'title': 'Deep learning for protein design'}
        def interrupted(venue, year, limit, existing, on_new, *, flush=None):
            on_new(row)
            raise RuntimeError('rate limited')
        with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as tmp:
            with patch('academic._crawl_one_metadata', side_effect=interrupted), \
                    patch('academic.select_ai4s', side_effect=lambda rows: list(rows)) as select:
                with self.assertRaisesRegex(RuntimeError, 'rate limited'):
                    academic.crawl_metadata_venue('ncs', 2024, None, Path(tmp))
            result = json.loads((Path(tmp) / 'natcomputsci/2024/ai4s.json').read_text())
            self.assertEqual(result[0]['id'], row['id'])
            select.assert_called_once()

    def test_metadata_failure_continues_other_sources_but_exits_nonzero(self):
        argv = ['academic.py', '-v', 'ncs,nmi', '-y', '2025', '--metadata-only']
        with patch('sys.argv', argv), patch('academic.logger'), \
                patch('academic.crawl_metadata_venue', side_effect=[RuntimeError('failed'), []]) as crawl, \
                patch('academic.write_run_status'), patch('academic.write_merged') as merge:
            with self.assertRaises(SystemExit) as exc:
                academic.main()
        self.assertEqual(exc.exception.code, 1)
        self.assertEqual(crawl.call_count, 2)
        merge.assert_called_once()


if __name__ == '__main__':
    unittest.main()
