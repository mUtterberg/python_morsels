from typing import Any, Callable, Iterable, NamedTuple


class MinMax(NamedTuple):
    """Unpackable tuple with named attributes"""
    min: Any
    max: Any


def minmax(in_obj: Iterable, *, key: Callable = None) -> MinMax:
    """Find min & max of list"""

    iter_obj = iter(in_obj)

    try:
        min_obj = max_obj = next(iter_obj)
        trans_min = trans_max = key(min_obj) if key else min_obj

    except StopIteration as stop_iter_e:
        raise ValueError('Empty iterable') from stop_iter_e

    for obj in iter_obj:

        trans_obj = key(obj) if key else obj

        if trans_obj < trans_min:
            trans_min, min_obj = trans_obj, obj

        if trans_obj > trans_max:
            trans_max, max_obj = trans_obj, obj

    return MinMax(min_obj, max_obj)


if __name__ == "__main__":
    pass
