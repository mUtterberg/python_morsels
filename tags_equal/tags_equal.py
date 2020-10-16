# pylint: disable=missing-module-docstring


from typing import List


def validate_tag_and_strip(is_tag: str) -> List[str]:
    """Validate & strip outer syntax"""
    if is_tag[0] != '<':
        raise SyntaxError('HTML tag must open with "<"')
    if is_tag[-1] != '>':
        raise SyntaxError('HTML tag must close with ">"')
    return sorted(is_tag[1:-1].lower().split(' '))


def tags_equal(html_a: str, html_b: str) -> bool:
    """Compare html opening tags"""
    equal = True
    tag_a = validate_tag_and_strip(html_a)
    tag_b = validate_tag_and_strip(html_b)
    for a, b in zip(tag_a, tag_b):
        if a != b:
            equal = False
    return equal


if __name__ == "__main__":
    print(validate_tag_and_strip('<HTML '))
