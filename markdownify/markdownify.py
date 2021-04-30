from html.parser import HTMLParser
from typing import List, Optional, Tuple


class MarkdownifyParser(HTMLParser):
    """Wrap HTMLParser for desired behavior"""

    processed_text = ''

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag == 'br':
            self.processed_text = self.processed_text.strip() + ' '

    def handle_data(self, data) -> None:
        self.processed_text += data.replace('\n', ' ')

    def handle_endtag(self, tag: str) -> None:
        if tag == 'p':
            self.processed_text += '\n\n'

    def consolidate_processed(self) -> None:
        """Whitespace normalization"""

    @property
    def markdown(self) -> str:
        """Convert processed lines to markdown string"""
        # return '\n\n'.join(self.processed_lines)
        return self.processed_text.strip()


def markdownify(html_str: str) -> str:
    """Convert HTML to markdown"""
    parser = MarkdownifyParser()
    parser.feed(html_str)
    parser.close()
    return parser.markdown


def run_examples() -> None:
    """Run some examples!"""
    html = (
        '<p>A paragraph<br><br>' +
        ' of text</p>' +
        '<p>Another paragraph</p>'
    )
    print(markdownify(html))


if __name__ == '__main__':
    run_examples()
