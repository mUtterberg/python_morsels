from collections import UserList
from itertools import cycle, islice
from typing import Any, Iterable, List, Union


class CyclicList(UserList):
    """Sort of like a list except that looping over it will result in an infinite loop."""

    def __init__(self, iter_input: Iterable[Any]) -> None:
        super().__init__(iter_input)
        self._data = iter_input
        # self.data = iter_input

    def __iter__(self) -> Any:
        this_iter = cycle(self._data)
        for item in this_iter:
            yield item

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, index_val: Union[int, slice]):
        if isinstance(index_val, slice):
            return self.__slice__(index_val.start, index_val.stop)
        try:
            return self._data[index_val]
        except IndexError:
            return self._data[index_val % len(self._data)]

    def __setitem__(self, index_val: int, item: Any):
        try:
            self._data[index_val] = item
        except IndexError:
            self._data[index_val % len(self._data)] = item

    def __slice__(self, start: int, stop: int) -> List[Any]:

        if not any((start, stop)):
            return self._data[:]

        if start is None:
            start = 0
        if stop is None:
            if start < 0:
                stop = 0
            else:
                stop = -1

        if 0 <= start <= len(self._data):
            if int(-1) <= stop <= len(self._data):
                print('Returning standard slice')
                return self._data[start:stop]
            return [self[i] for i in range(start, stop)]
        return [self[i] for i in range(start, stop)]


    def append(self, new_item):
        """Append data"""
        self._data.append(new_item)

    def pop(self, pop_index=None):
        """Pop"""
        try:
            return self._data.pop(pop_index)
        except TypeError:
            return self._data.pop()


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
