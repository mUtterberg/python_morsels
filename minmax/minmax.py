from typing import Any, Callable, Iterable, NamedTuple


class MinMax(NamedTuple):
    """Unpackable tuple with named attributes"""
    min: Any
    max: Any


def identity(obj: Any) -> Any:
    """Identity as default key"""
    return obj


def minmax(in_obj: Iterable, *, key: Callable = identity) -> MinMax:
    """Find min & max of list"""

    trans_min = None
    trans_max = None
    min_obj = None
    max_obj = None

    for next_obj in in_obj:
        trans_obj = key(next_obj)
        if (trans_min is None) or (trans_obj < trans_min):
            trans_min = trans_obj
            min_obj = next_obj

        if (max_obj is None) or (trans_obj > trans_max):
            trans_max = trans_obj
            max_obj = next_obj

    if (min_obj is None) or (max_obj is None):
        raise ValueError('Empty iterable')

    return MinMax(min_obj, max_obj)


if __name__ == "__main__":
    pass
