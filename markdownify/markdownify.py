from html.parser import HTMLParser
from typing import List, Optional, Tuple


class MarkdownifyParser(HTMLParser):
    """Wrap HTMLParser for desired behavior"""

    processed_text = ''
    link_url = ''

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag == 'br':
            self.processed_text = self.processed_text.strip() + '  \n'
        elif tag == 'strong':
            self.processed_text += '**'
        elif tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.link_url = attr[-1]
                    break
            self.processed_text += '['

    def handle_data(self, data) -> None:
        self.processed_text += data.replace('\n', ' ')

    def handle_endtag(self, tag: str) -> None:
        if tag == 'p':
            self.processed_text += '\n\n'
        elif tag == 'strong':
            self.processed_text += '**'
        elif tag == 'a':
            self.processed_text += f']({self.link_url})'
            self.link_url = ''

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
    print(markdownify('<a href="http://www.treyhunner.com">Trey</a> has a blog'))


if __name__ == '__main__':
    run_examples()
