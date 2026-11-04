import http.client
import json
import tempfile
import threading
import unittest
from pathlib import Path
from http.server import ThreadingHTTPServer

from monitor_server import Collector, make_handler, read_counts, redact


class MonitorTests(unittest.TestCase):
    def test_current_status_overrides_errors_from_an_earlier_attempt(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as tmp:
            root = Path(tmp)
            (root / 'manifest.json').write_text('{"year":2024,"sources":["a","b"]}')
            folder = root / 'metadata/2024'
            folder.mkdir(parents=True)
            (folder / 'run-status.json').write_text('[{"source":"a","state":"completed"},{"source":"b","state":"pending"}]')
            dest = root / 'metadata/a/2024'
            dest.mkdir(parents=True)
            (dest / 'papers.json').write_text('[]')
            (dest / 'ai4s.json').write_text('[]')
            (root / 'crawl.log').write_text('old - a 元数据抓取失败\nold - b 元数据抓取失败\n', encoding='utf-8')
            result = Collector(root / 'metadata', root / 'manifest.json', root / 'crawl.log',
                               lambda: {'ActiveState': 'active'}).collect()
            self.assertEqual(result['failed_sources'], 0)
            self.assertEqual([r['status'] for r in result['sources']], ['completed', 'pending'])

    def test_upstream_retries_are_surfaced_without_failing_sources(self):
        from datetime import datetime
        stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'manifest.json').write_text('{"year":2024,"sources":["iros","embc"]}')
            folder = root / 'metadata/2024'
            folder.mkdir(parents=True)
            (folder / 'run-status.json').write_text(
                '[{"source":"iros","state":"running"},{"source":"embc","state":"retryable"}]')
            log = root / 'crawl.log'
            log.write_text(
                f'{stamp}.035 | WARNING  | conference_meta:_page_payload:41 - iros 2024: DBLP 枚举第 3 次失败（ReadTimeout），40 秒后重试\n'
                f'{stamp}.091 | WARNING  | conference_meta:_page_payload:41 - embc 2024: DBLP 枚举第 1 次失败（HTTPError），10 秒后重试\n'
                f'{stamp}.500 | WARNING  | academic:main:444 - 第 2 轮重试上游暂时不可用的来源（1 个）: embc\n',
                encoding='utf-8')
            result = Collector(root / 'metadata', root / 'manifest.json', log,
                               lambda: {'ActiveState': 'active', 'SubState': 'running'}).collect()
            self.assertEqual({row['source']: row['status'] for row in result['sources']},
                             {'iros': 'retrying', 'embc': 'retrying'})
            self.assertEqual(result['retry_round'], 2)
            self.assertEqual({row['source']: row['attempt'] for row in result['retrying_sources']},
                             {'iros': 3, 'embc': 1})
            self.assertEqual({row['source']: row['error'] for row in result['retrying_sources']},
                             {'iros': 'ReadTimeout', 'embc': 'HTTPError'})
            self.assertEqual(result['failed_sources'], 0)

    def test_counts_stream_records_with_nested_data(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'papers.json'
            path.write_text(json.dumps([
                {'id': '1', 'abstract': 'A } quoted " phrase', 'nested': [{'id': 'x'}]},
                {'id': '2', 'abstract': None},
            ]), encoding='utf-8')
            self.assertEqual(read_counts(path), (2, 1, 0))
            path.write_text('[{"id":', encoding='utf-8')
            with self.assertRaises(ValueError):
                read_counts(path)

    def test_collector_distinguishes_checkpoint_completion_and_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = root / 'manifest.json'
            manifest.write_text(json.dumps({'year': 2024, 'sources': ['a', 'b', 'c']}))
            log = root / 'crawl.log'
            log.write_text('academic:crawl_metadata_venue:1 - b 元数据抓取失败\n', encoding='utf-8')
            for name in ('a', 'b'):
                dest = root / 'metadata' / name / '2024'
                dest.mkdir(parents=True)
                (dest / 'papers.json').write_text('[{"id":"1","abstract":"yes"}]')
            (root / 'metadata/a/2024/ai4s.json').write_text('[]')
            # An annual merge must not be counted as another source.
            (root / 'metadata/2024').mkdir()
            (root / 'metadata/2024/papers.json').write_text('[{},{}]')
            collector = Collector(root / 'metadata', manifest, log,
                                  lambda: {'ActiveState': 'active', 'SubState': 'running'})
            result = collector.collect()
            self.assertEqual(result['saved_papers'], 2)
            self.assertEqual(result['completed_sources'], 1)
            self.assertEqual(result['failed_sources'], 1)
            self.assertEqual(result['total_sources'], 3)
            self.assertEqual({r['source']: r['status'] for r in result['sources']},
                             {'a': 'completed', 'b': 'failed', 'c': 'pending'})
            self.assertEqual([r['ai4s_ready'] for r in result['sources']], [True, False, False])
            self.assertEqual(result['service']['state'], 'running')

    def test_malformed_checkpoint_is_visible(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'manifest.json').write_text('{"year":2024,"sources":["a"]}')
            dest = root / 'metadata/a/2024'
            dest.mkdir(parents=True)
            (dest / 'papers.json').write_text('[invalid]')
            collector = Collector(root / 'metadata', root / 'manifest.json', root / 'missing.log',
                                  lambda: {'ActiveState': 'inactive', 'Result': 'success', 'ExecMainStatus': '0'})
            result = collector.collect()
            self.assertEqual(result['sources'][0]['status'], 'unreadable')
            self.assertEqual(result['service']['state'], 'finished')

    def test_backfill_jobs_are_reported_with_progress(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'manifest.json').write_text('{"year":2024,"sources":["j-1","j-2"]}')
            for name, rows in (('j-1', [{'doi': 'a', 'abstract': None}, {'doi': 'b', 'abstract': 'x'}]),
                              ('j-2', [{'doi': 'c'}])):
                dest = root / 'metadata' / name / '2024'
                dest.mkdir(parents=True)
                (dest / 'papers.json').write_text(json.dumps(rows))
            (root / 'metadata/backfill-jobs.json').write_text(json.dumps({
                'started_at': '2026-11-04 19:46:02',
                'folders': [{'source': 'j-1', 'title': 'Journal One', 'missing_start': 4},
                            {'source': 'j-2', 'title': 'Journal Two', 'missing_start': 3}]}))
            result = Collector(root / 'metadata', root / 'manifest.json', root / 'absent.log',
                               lambda: {'ActiveState': 'active'}).collect()
            jobs = {job['source']: job for job in result['backfill']['jobs']}
            self.assertEqual(result['missing_with_doi'], 2)
            self.assertEqual(jobs['j-1']['missing_now'], 1)
            self.assertEqual(jobs['j-1']['filled'], 3)
            self.assertEqual(jobs['j-1']['title'], 'Journal One')
            self.assertEqual(jobs['j-1']['status'], 'running')
            self.assertEqual(jobs['j-2']['missing_start'], 3)
            self.assertEqual(result['backfill']['total_filled'], 5)

    def test_backfill_is_derived_from_gaps_when_no_job_file_exists(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'manifest.json').write_text('{"year":2024,"sources":["j-1","cvpr"]}')
            for name, rows in (('j-1', [{'doi': 'a'}, {'doi': 'b'}, {'abstract': 'x'}]),
                               ('cvpr', [{'doi': 'c'}])):
                dest = root / 'metadata' / name / '2024'
                dest.mkdir(parents=True)
                (dest / 'papers.json').write_text(json.dumps(rows))
            result = Collector(root / 'metadata', root / 'manifest.json', root / 'absent.log',
                               lambda: {'ActiveState': 'active'}).collect()
            self.assertEqual(result['backfill']['origin'], 'derived')
            self.assertEqual([job['source'] for job in result['backfill']['jobs']], ['j-1'])
            self.assertEqual(result['backfill']['jobs'][0]['status'], 'idle')

    def test_live_job_status_can_finish_with_gaps_and_lists_conference_reruns(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'manifest.json').write_text('{"year":2024,"sources":["j-1","iros","icc"]}')
            meta = root / 'metadata'
            (meta / '2024').mkdir(parents=True)
            (meta / '2024/run-status.json').write_text(
                '[{"source":"iros","state":"retryable"},{"source":"icc","state":"running"}]')
            dest = meta / 'j-1/2024'
            dest.mkdir(parents=True)
            (dest / 'papers.json').write_text('[{"doi":"a"}]')
            (meta / 'backfill-jobs.json').write_text(
                '{"folders":[{"source":"j-1","missing_start":2,"status":"done"}]}')
            result = Collector(meta, root / 'manifest.json', root / 'absent.log',
                               lambda: {'ActiveState': 'active'}).collect()
            self.assertEqual(result['backfill']['jobs'][0]['status'], 'done')
            self.assertEqual(result['backfill']['total_missing_now'], 1)
            self.assertEqual({row['source']: row['status'] for row in result['retrying_sources']},
                             {'iros': 'queued', 'icc': 'collecting'})

    def test_concurrent_run_status_marks_all_active_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'manifest.json').write_text('{"year":2024,"sources":["a","b"]}')
            dest = root / 'metadata/2024'
            dest.mkdir(parents=True)
            (dest / 'run-status.json').write_text('[{"source":"a","state":"running"},{"source":"b","state":"running"}]')
            result = Collector(root / 'metadata', root / 'manifest.json', root / 'missing.log',
                               lambda: {'ActiveState': 'active'}).collect()
            self.assertEqual(set(result['current_sources']), {'a', 'b'})
            self.assertTrue(all(row['status'] == 'collecting' for row in result['sources']))

    def test_event_not_held_counts_as_processed_not_failed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'manifest.json').write_text('{"year":2024,"sources":["iccv"]}')
            folder = root / 'metadata/2024'
            folder.mkdir(parents=True)
            (folder / 'run-status.json').write_text('[{"source":"iccv","state":"not_held"}]')
            result = Collector(root / 'metadata', root / 'manifest.json', root / 'absent.log',
                               lambda: {'ActiveState': 'active', 'MemoryMax': str(8 * 1024**3),
                                        'CPUQuotaPerSecUSec': '16s'}).collect()
            self.assertEqual(result['sources'][0]['status'], 'not_held')
            self.assertEqual(result['completed_sources'], 1)
            self.assertEqual(result['failed_sources'], 0)
            self.assertEqual(result['service']['memory_limit_bytes'], 8 * 1024**3)
            self.assertEqual(result['service']['cpu_limit_cores'], 16)

    def test_log_secrets_are_not_displayed(self):
        self.assertNotIn('secret', redact('Authorization: Bearer secret'))
        self.assertNotIn('secret', redact('OPENREVIEW_PASSWORD=secret'))
        self.assertEqual(redact('403 Forbidden for paper DOI'), '403 Forbidden for paper DOI')

    def test_warning_and_error_counts_are_separate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'manifest.json').write_text('{"year":2024,"sources":[]}')
            (root / 'metadata').mkdir()
            (root / 'crawl.log').write_text('time | WARNING | one\ntime | ERROR | two\ntime | INFO | three\n')
            result = Collector(root / 'metadata', root / 'manifest.json', root / 'crawl.log',
                               lambda: {'ActiveState': 'active'}).collect()
            self.assertEqual(result['recent_warnings'], 1)
            self.assertEqual(result['recent_errors'], 1)
            self.assertEqual(len(result['logs']), 3)

    def test_http_requires_secret_for_every_endpoint_and_is_read_only(self):
        secret = 'a' * 64
        class FakeCollector:
            snapshot = {'saved_papers': 12}
        server = ThreadingHTTPServer(('127.0.0.1', 0), make_handler(secret, FakeCollector()))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            client = http.client.HTTPConnection('127.0.0.1', server.server_port, timeout=3)
            for path in ('/', '/academic-watch/wrong/status', '/academic-watch/' + secret + 'extra/status',
                         '/academic-watch/' + secret + '/../monitor_server.py'):
                client.request('GET', path)
                response = client.getresponse()
                self.assertEqual(response.status, 404, path)
                response.read()
            client.request('GET', '/academic-watch/' + secret + '/status')
            response = client.getresponse()
            self.assertEqual(response.status, 200)
            self.assertEqual(response.getheader('Cache-Control'), 'no-store')
            self.assertEqual(response.getheader('Referrer-Policy'), 'no-referrer')
            self.assertEqual(json.loads(response.read())['saved_papers'], 12)
            client.request('GET', '/academic-watch/' + secret + '/')
            response = client.getresponse()
            self.assertEqual(response.status, 200)
            self.assertIn(b'2024', response.read())
            client.request('POST', '/academic-watch/' + secret + '/status')
            response = client.getresponse()
            self.assertEqual(response.status, 405)
            response.read()
            client.close()
        finally:
            server.shutdown()
            server.server_close()


if __name__ == '__main__':
    unittest.main()
