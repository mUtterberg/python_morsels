from typing import Any, Callable, Iterable, NamedTuple, Tuple, Union

SENTINEL = object()


class MinMax(NamedTuple):
    """Enable named attributes min & max"""
    min: Any
    max: Any


def minmax(*in_iter: Tuple[Union[Any, Iterable[Any]]], default: Any = SENTINEL, key: Callable = lambda s: s) -> MinMax:
    """Find min & max value in iterable"""

    if not in_iter:
        raise TypeError('minmax() has no args')
    if len(in_iter) == 1:
        in_iter = in_iter[0]

    if not in_iter:
        if default is SENTINEL:
            raise ValueError('minmax() arg is an empty iterable')
        return MinMax(default, default)

    trans_iter = [key(x) for x in in_iter]
    min_val = min(trans_iter)
    max_val = max(trans_iter)

    for val in in_iter:
        if key(val) == min_val:
            min_val = val
        if key(val) == max_val:
            max_val = val

    return MinMax(min_val, max_val)


if __name__ == '__main__':
    print(minmax())
