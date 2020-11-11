from typing import Sequence


def all_same(in_seq: Sequence) -> bool:
    """Determine if all elements are the same"""

    comp = next(iter(in_seq), None)
    return all(
        item == comp
        for item in in_seq
    )


def print_test(in_seq: Sequence) -> None:
    """Print test-case"""
    print(f'Test case "{in_seq}" :', all_same(in_seq))


if __name__ == "__main__":
    print_test([1, 1, 1])
    print_test([1, 0, 1])
    print_test([(1, 'a'), (1, 'a')])
    print_test([(1, 'a'), (1, 'b')])
