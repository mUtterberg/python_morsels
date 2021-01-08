from typing import Iterable


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
        for step in self.__iter__():
            yield step

    def _compare_step(self, this_step: float) -> bool:
        """Determine if element is in range"""
        if self._step > 0:
            if self._start <= this_step < self._stop:
                return True
            return False
        if self._start >= this_step > self._stop:
            return True
        return False

    def __getitem__(self, in_dex: int) -> float:
        if in_dex < 0:
            in_dex += len(self)
        value = self._start + self._step * in_dex
        if not self._compare_step(value):
            raise IndexError
        return value


if __name__ == "__main__":
    pass
