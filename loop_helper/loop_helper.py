from dataclasses import dataclass
from typing import Any, Iterable, Tuple


@dataclass
class LoopHelper:
    """Loop helper class"""

    index: int = 0
    is_first: bool = True

    def __iter__(self):
        yield self
        self.index += 1
        self.is_first = False

    def __next__(self):
        yield self.index
        self.index += 1

    def increment(self):
        """Increment values"""
        self.index += 1
        self.is_first = False

    def reset(self):
        """Reset values"""
        self.index = 0
        self.is_first = True


def loop_helper(in_iter: Iterable) -> Tuple[Any, LoopHelper]:
    """Provide commonly-used information while looping"""

    loop_status = LoopHelper()
    for value in in_iter:
        yield value, loop_status
        loop_status.increment()


COLORS = ["red", "blue", "green"]


def check_progress():
    """Case checker"""

    for color, info in loop_helper(COLORS):
        if info.is_first:
            print('This is the first color!')
        print(f'Color {info.index} is {color}')


if __name__ == '__main__':
    check_progress()
