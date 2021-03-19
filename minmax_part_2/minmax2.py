from typing import Any, Callable, Iterable, Tuple

SENTINEL = object()


def minmax(in_iter: Iterable[Any], *, default: Any = SENTINEL, key: Callable = lambda s: s) -> Tuple[Any, Any]:
    """Not sure yet"""

    if not in_iter:
        if default == SENTINEL:
            raise ValueError('minmax() arg is an empty iterable')
        return default, default

    trans_iter = [key(x) for x in in_iter]
    min_val = min(trans_iter)
    max_val = max(trans_iter)

    for val in in_iter:
        if key(val) == min_val:
            min_val = val
        if key(val) == max_val:
            max_val = val

    return min_val, max_val


if __name__ == '__main__':
    pass
