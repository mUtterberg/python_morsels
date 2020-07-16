

from typing import Type


class float_range:

    def __init__(self, input_start, input_end=None, input_step=1) -> None:
        if isinstance(input_end, type(None)):
            input_end = input_start
            input_start = 0
        self.start = input_start
        self.current = input_start
        self.end = input_end
        self.step = input_step
        self.pos = bool(input_step > 0)
        # self.data = iter([])

    def __len__(self):
        length = (self.end - self.start) // self.step
        if length >= 0:
            return length
        return -length

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current
        if self.pos and (current < self.end):
            self.current += self.step
            return current
        if (not self.pos) and (current > self.end):
            self.current += self.step
            return current
        raise StopIteration

    def __reversed__(self):
        start = self.end
        self.end = self.start
        self.start = start
        self.step = -self.step
        self.pos = -self.pos


if __name__ == "__main__":
    TEST = len(float_range(10))
    print(TEST)

    TEST = len(float_range(1, 11, -10))
    print(TEST)

    print(len(float_range(5, 0, -1)))
    
    TEST = list(float_range(5, 0, -1))
    print(TEST)
