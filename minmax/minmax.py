from typing import Any, Callable, Iterable, NamedTuple


class MinMax(NamedTuple):
    """Unpackable tuple with named attributes"""
    min: Any
    max: Any


def minmax(in_obj: Iterable, *, key: Callable = None) -> MinMax:
    """Find min & max of list"""

    min_obj = None
    max_obj = None

    if key is None:
        for next_obj in in_obj:
            if (min_obj is None) or (next_obj < min_obj):
                min_obj = next_obj

            if (max_obj is None) or (next_obj > max_obj):
                max_obj = next_obj

    else:

        trans_obj = iter(key(x) for x in in_obj)

        min_orig = None
        max_orig = None
        for next_obj, next_orig in zip(trans_obj, in_obj):
            if (min_obj is None) or (next_obj < min_obj):
                min_obj = next_obj
                min_orig = next_orig

            if (max_obj is None) or (next_obj > max_obj):
                max_obj = next_obj
                max_orig = next_orig

        min_obj = min_orig
        max_obj = max_orig

    if (min_obj is None) or (max_obj is None):
        raise ValueError('Empty iterable')

    return MinMax(min_obj, max_obj)


if __name__ == "__main__":
    pass
