from typing import Sequence


def all_same(in_seq: Sequence) -> bool:
    """Determine if all elements are the same"""

    in_seq = iter(in_seq)
    try:
        comp = next(in_seq)
    except StopIteration:
        return True
    for item in in_seq:
        if item != comp:
            return False
    return True


def print_test(in_seq: Sequence) -> None:
    """Print test-case"""
    print(f'Test case "{in_seq}" :', all_same(in_seq))


if __name__ == "__main__":
    print_test([1, 1, 1])
    print_test([1, 0, 1])
    print_test([(1, 'a'), (1, 'a')])
    print_test([(1, 'a'), (1, 'b')])
