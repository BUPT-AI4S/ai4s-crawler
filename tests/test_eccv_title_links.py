import unittest

from eccv_meta import parse_accepted_html


class AcceptedPaperTitleTests(unittest.TestCase):
    def test_projection_titles_are_papers_and_project_links_stay_separate(self):
        page = '''<table>
          <tr><td><a href="/virtual/2026/poster/4570">RayRoPE: Projective Ray Encoding</a>
            <a href="https://example.org/project" data-elc-skip>Project Page ↗</a>
            <div class="indented">First Author</div></td><td>3D geometry</td></tr>
          <tr><td><a href="/virtual/2026/poster/4820">Two Birds, One Projection</a>
            <a href="https://example.org/second">Project Website</a></td><td>Vision</td></tr>
        </table>'''
        rows = parse_accepted_html(page, 'https://eccv.ecva.net/Conferences/2026/AcceptedPapers')
        self.assertEqual([r['title'] for r in rows],
                         ['RayRoPE: Projective Ray Encoding', 'Two Birds, One Projection'])
        self.assertEqual(rows[0]['url'], 'https://eccv.ecva.net/virtual/2026/poster/4570')
        self.assertEqual(rows[0]['project_url'], 'https://example.org/project')
        self.assertEqual(rows[1]['project_url'], 'https://example.org/second')

    def test_privacy_table_row_is_not_a_paper(self):
        page = '''<table><tr>
          <td><a href="/public/PrivacyPolicy">Our Privacy Policy »</a></td>
          <td>Privacy information</td>
        </tr></table>'''
        self.assertEqual(parse_accepted_html(page, 'https://eccv.ecva.net/Conferences/2026/AcceptedPapers'), [])


if __name__ == '__main__':
    unittest.main()
