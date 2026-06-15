from django.test import SimpleTestCase

from torvu.templatetags.markdown_extras import markdown_filter


class MarkdownFilterTests(SimpleTestCase):
    def test_markdown_filter_renders_paragraphs_lists_and_tables(self):
        value = """
First paragraph with **bold** text.

Second paragraph.

- one
- two

| Name | Value |
| --- | --- |
| A | 1 |
"""

        rendered = markdown_filter(value)

        self.assertIn("<p>First paragraph with <strong>bold</strong> text.</p>", rendered)
        self.assertIn("<p>Second paragraph.</p>", rendered)
        self.assertIn("<ul>", rendered)
        self.assertIn("<li>one</li>", rendered)
        self.assertIn("<table>", rendered)
        self.assertIn("<th>Name</th>", rendered)
