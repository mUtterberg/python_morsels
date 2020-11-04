from collections import OrderedDict
from collections.abc import MutableSet
from typing import Any, Iterable, TypeVar

_T = TypeVar('_T')


class OrderedSet(MutableSet):
    """Like a set, but ordered!"""

    def __init__(self, iter_in: Iterable = ()) -> None:
        self.data = OrderedDict.fromkeys(iter_in, None)

    def __iter__(self) -> Iterable:
        for item in self.data:
            yield item

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return f'OrderedSet({list(self.data)})'

    def __contains__(self, item: Any) -> bool:
        try:
            self.data[item]
            return True
        except KeyError:
            return False

    def __eq__(self, o: object) -> bool:
        try:
            return self.data == o.data
        except AttributeError:
            return o == set(self.data)

    def add(self, value: _T) -> None:
        """Add unique data to self.data"""
        self.data.setdefault(value)

    def discard(self, value: _T) -> None:
        """Remove data from self.data"""
        self.data.pop(value, None)


if __name__ == "__main__":
    TEST_ITER = []
    print(*OrderedSet(TEST_ITER))
    TEST_ITER += ['these', 'words', 'are', 'in', 'an', 'order']
    print(*OrderedSet(TEST_ITER))

    print(OrderedSet('abc') == OrderedSet('bac'))
