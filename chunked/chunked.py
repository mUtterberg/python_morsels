from collections import deque
from typing import Generator, Sequence, Union


def chunked(in_list: Union[Generator, Sequence], n_width: int, **kwargs) -> Generator:  # pylint: disable=unused-argument
    """Accepts a sequence and a number, returns one list-of-lists"""
    this_group = deque(maxlen=n_width)
    rem = 0
    first = True
    for i_x, val in enumerate(in_list):
        this_group.append(val)
        rem = (i_x + 1) % n_width  # type: int
        if rem == 0:
            first = False
            yield tuple(this_group)
    if not first:
        for i_x in range(rem):
            if 'fill' in kwargs:
                this_group.append(kwargs['fill'])
            else:
                this_group.popleft()
    if this_group and (rem != 0):
        yield tuple(this_group)


if __name__ == "__main__":
    # print(list(chunked('abcdefg', 3, fill=0)))
    # print(list(chunked('abcdefg', 3, 0)))
    # print(list(chunked([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, fill=5)))
    print(list(chunked([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15)))
    print(list(chunked((n**2 for n in range(10)), 4, fill=None)))
