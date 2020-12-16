from collections import deque
from typing import Any, Iterable, Iterator


def window(numbers: Iterable, width: int, *, fillvalue: Any = None) -> Iterator:
    """Return windows of width consecutive items in numbers"""

    if width != 0:

        counter = 0
        return_val = deque(maxlen=width)

        for item in numbers:
            return_val.append(item)
            counter += 1
            if counter >= width:
                yield tuple(return_val)

        diff = width - len(return_val)
        if diff > 0:
            yield tuple(list(return_val) + [fillvalue for n in range(diff)])


if __name__ == "__main__":
    # NUMBERS = [1, 2, 3, 4, 5, 6]
    print(list(window([1, 2, 3], 6)))
