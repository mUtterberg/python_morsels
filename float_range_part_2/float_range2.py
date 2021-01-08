from typing import Iterable, Iterator, List, Union


class float_range:
    """Like range() but for floats (part 2)"""

    def __init__(self, start: float, stop: float = None, step: float = 1) -> None:
        if stop is None:
            self._start = 0
            self._stop = start
        else:
            self._start = start
            self._stop = stop
        self._step = step

    @property
    def _items(self):
        """Return list of items"""
        return list(self.__iter__())

    def __len__(self) -> int:
        length = (self._stop - self._start) / self._step
        if length < 0:
            return 0
        if length % 1 > 0:
            return int(length) + 1
        return int(length)

    def __iter__(self) -> Iterable:
        this_step = self._start
        while self._compare_step(this_step):
            yield this_step
            this_step += self._step

    def __next__(self):
        for step in iter(self):
            yield step

    def __reversed__(self):
        return iter(float_range(self.__getitem__(-1), self._start - self._step, self._step * -1))

    def _compare_step(self, this_step: float) -> bool:
        """Determine if element is in range"""
        if self._step > 0:
            if self._start <= this_step < self._stop:
                return True
            return False
        if self._start >= this_step > self._stop:
            return True
        return False

    def _get(self, in_dex: int) -> float:
        """Get single index"""
        if in_dex < 0:
            in_dex += len(self)
        value = self._start + self._step * in_dex
        if not self._compare_step(value):
            raise IndexError
        return value

    def __getitem__(self, item: Union[int, slice]) -> Union[List[float], float]:
        if isinstance(item, int):
            return self._get(item)
        if isinstance(item, slice):
            return_val = []
            start = 0
            stop = len(self)
            stride = 1
            if item.start is not None:
                start = item.start
                if start < 0:
                    start = len(self) + item.start
                    if start < 0:
                        start = len(self)
            if item.stop is not None:
                stop = item.stop
                if stop > len(self):
                    stop = len(self)
            if item.step is not None:
                stride = item.step
            for in_dex in range(start, stop, stride):
                if in_dex < 0:
                    in_dex += len(self)
                value = self._start + self._step * in_dex
                if not self._compare_step(value):
                    raise IndexError
                return_val.append(value)
            return return_val
        else:
            raise TypeError


if __name__ == "__main__":
    pass
