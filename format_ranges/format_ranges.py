from typing import Iterable, Tuple


def group_consecutive(input_list: Iterable[int]) -> Tuple[int, int]:
    """Generator to yield tuple of consecutive integers in iterable"""
    duplicates = []
    first = next(input_list)
    prev = first
    try:
        while item:= next(input_list):
            if item == prev + 1:
                prev = item
                continue
            if item == prev:
                duplicates.append(item)
                continue

            yield first, prev
            first = item
            prev = item

    except StopIteration:
        yield first, prev
    if duplicates:
        new_ranges = group_consecutive(iter(duplicates))
        for new_range in new_ranges:
            yield new_range


def format_ranges(input_range: Iterable[int]) -> str:
    """Format consecutive values in range"""
    list_consecutive = group_consecutive(iter(sorted(input_range)))
    string_ranges = [f'{x[0]}-{x[1]}' if x[0] != x[1] else str(x[0]) for x in sorted(list_consecutive)]
    output_string = ','.join(string_ranges)

    return output_string


if __name__ == "__main__":
    test_list = [1, 1, 2, 2, 3, 4, 4, 7, 7, 8, 9]
    print(format_ranges(test_list))
