# pylint: disable=missing-module-docstring


import shlex
from html.parser import HTMLParser
from typing import Dict, List, Optional, Tuple


class TagParser(HTMLParser):
    """Parse HTML opening tags"""

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        """Overload HTMLParser handle_starttag method"""
        self.value = (tag, dict(reversed(attrs)))


def parse_tag(html_tag: str) -> Tuple[str, Dict[str, str]]:
    """Return tuple of tag name and sorted attributes"""
    parser = TagParser()
    parser.feed(html_tag)
    return parser.value


def validate_tag_and_strip(is_tag: str) -> Dict[str, str]:
    """Validate & strip outer syntax"""
    if is_tag[0] != '<':
        raise SyntaxError('HTML tag must open with "<"')
    if is_tag[-1] != '>':
        raise SyntaxError('HTML tag must close with ">"')
    tags = shlex.split(is_tag[1:-1].lower())
    return dict(
        tag.split('=') if '=' in tag else [tag, tag]
        for tag in reversed(tags)
    )


def tags_equal(html_a: str, html_b: str) -> bool:
    """Compare html opening tags"""
    # tag_a = validate_tag_and_strip(html_a)
    # tag_b = validate_tag_and_strip(html_b)
    tag_a = parse_tag(html_a)
    tag_b = parse_tag(html_b)
    equal = tag_a == tag_b
    return equal


if __name__ == "__main__":
    print(tags_equal(
        '<label for=id_email for=id_username>',
        '<label for=id_email>'
    ))
