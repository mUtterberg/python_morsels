from collections import deque
from typing import Any, Iterator, List, Optional, Tuple


def window(numbers: List[Any], width: int) -> Iterator[Optional[Tuple[Any]]]:
    """Window"""
    if width == 0:
        yield None
    val_window = deque(maxlen=width)
    can_stop = False
    for value in numbers:
        val_window.append(value)
        if len(val_window) == width:
            can_stop = True
            yield tuple(val_window)
        elif can_stop:
            raise StopIteration


if __name__ == "__main__":
    NUM_WINDOW = window([1, 2, 3, 4, 5, 6], 2)
    print(next(NUM_WINDOW))
    print(next(NUM_WINDOW))
    print(next(NUM_WINDOW))
