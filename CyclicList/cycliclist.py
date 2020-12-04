from collections import UserList
from itertools import islice
from typing import Any, Tuple, Union


class CyclicList(UserList):  # pylint: disable=too-many-ancestors
    """Sort of like a list except that looping over it will result in an infinite loop."""

    def __getitem__(self, index_val: Union[int, slice]):
        if isinstance(index_val, slice):
            return [self[i] for i in range(*self._slice_indices(index_val))]
        return self.data[index_val % len(self)]

    def __setitem__(self, index_val: int, item: Any):
        self.data[index_val % len(self)] = item

    def _slice_indices(self, obj: slice) -> Tuple[int, int, int]:

        if obj.step is not None:
            raise ValueError('Step not supported.')

        start, stop = obj.start, obj.stop

        if start is None:
            start = 0
        if stop is None:
            if start < 0:
                stop = 0
            else:
                stop = len(self)

        return start, stop, 1


def run_local_review():
    """Run examples from exercise description"""
    my_list = CyclicList([1, 2, 3])
    for i, num in enumerate(my_list):
        print(num)
        if i > 8:
            break

    print()

    print(list(islice(my_list, 5)))

    print()

    my_list.append(4)
    print(my_list.pop())
    print(len(my_list))
    print(my_list.pop(0))
    print(len(my_list))

    print()

    my_list = CyclicList([1, 2, 3])
    print(my_list[1])
    print(my_list[-1])
    print(my_list[5])
    print(my_list[-4])

    print()

    my_list = CyclicList([1, 2, 3])
    print(my_list[-2:])
    print(my_list[:8])
    print(my_list[-2:2])
    print(my_list[:-1])

    print()

    my_list = CyclicList([1, 2, 3])
    print(my_list[-3:])


if __name__ == "__main__":
    run_local_review()
