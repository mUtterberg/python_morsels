# pylint: disable=missing-module-docstring


import shlex
from typing import Dict


def validate_tag_and_strip(is_tag: str) -> Dict[str, str]:
    """Validate & strip outer syntax"""
    if is_tag[0] != '<':
        raise SyntaxError('HTML tag must open with "<"')
    if is_tag[-1] != '>':
        raise SyntaxError('HTML tag must close with ">"')
    tags = reversed(shlex.split(is_tag[1:-1].lower()))
    return {
        x.split('=')[0]:x.split('=')[-1]
        for x in tags
        }


def tags_equal(html_a: str, html_b: str) -> bool:
    """Compare html opening tags"""
    tag_a = validate_tag_and_strip(html_a)
    tag_b = validate_tag_and_strip(html_b)
    equal = tag_a == tag_b
    return equal


if __name__ == "__main__":
    print(tags_equal(
        '<label for=id_email for=id_username>',
        '<label for=id_email>'
    ))
