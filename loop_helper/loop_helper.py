from dataclasses import dataclass
from typing import Any, Iterable, Iterator, Tuple


SENTINEL = object()


@dataclass
class LoopHelper:
    """Loop helper class"""

    previous_default: Any
    next_default: Any
    index: int = 0
    is_first: bool = True
    is_last: bool = False
    current: Any = SENTINEL
    previous: Any = SENTINEL
    next: Any = SENTINEL

    def __init__(self, previous_default, next_default) -> None:
        self.previous_default = previous_default
        self.next_default = next_default

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     index = self.index
    #     self.index += 1
    #     return index

    def increment(self):
        """Increment values"""
        self.index += 1
        self.is_first = False

    def update(self, value: Any):
        """Set current"""
        self.previous = self.previous_default if self.current is SENTINEL else self.current
        self.current = value

    def preview(self, value: Any):
        """Set next"""
        self.next = value

    def reset(self):
        """Reset values"""
        self.index = 0
        self.is_first = True


def loop_helper(
        in_iter: Iterable[Any], previous_default: Any = None, next_default: Any = None
    ) -> Iterator[Tuple[Any, LoopHelper]]:
    """Provide commonly-used information while looping"""

    loop_status = LoopHelper(previous_default, next_default)
    if not isinstance(in_iter, Iterator):
        in_iter = iter(in_iter)

    try:
        return_value = next(in_iter)
    except StopIteration:
        return

    loop_status.update(return_value)

    for value in in_iter:
        loop_status.preview(value)
        yield return_value, loop_status
        return_value = value
        loop_status.update(value)
        loop_status.increment()

    loop_status.is_last = True
    loop_status.preview(next_default)
    yield return_value, loop_status


COLORS = ["red", "blue", "green"]


def check_progress():
    """Case checker"""

    for color, info in loop_helper(COLORS):
        if info.is_first:
            print(f'{color.title()} is the best color!')
        else:
            print(f'No {info.current} is the best color, not {info.previous}')
        # print(f'Color {info.index} is {color}')

        if info.is_last:
            print(f'Thanks {info.previous}. I\'m {color}, here\'s... {info.next}?')


if __name__ == '__main__':
    check_progress()
