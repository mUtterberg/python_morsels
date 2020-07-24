

class float_range:

    def __init__(self, input_start, input_end=None, input_step=1) -> None:
        if isinstance(input_end, type(None)):
            input_end = input_start
            input_start = 0
        self.start = input_start
        self.current = input_start
        self.stop = input_end
        self.step = input_step
        self.pos = bool(input_step > 0)
    
    def get_element(self, ix: int) -> float:
        return self.start + self.step * ix

    def __reversed__(self):
        for x in range(len(self)):
            yield self.get_element(len(self) - x - 1)

    def __eq__(self, value):
        try:
            same_length = (len(self) == len(value))
            same_start = (self.start == value.start)
            if same_length:
                if not len(self):
                    return True
                elif (len(self) == 1) and same_start:
                    return True
            same_step = (self.step == value.step)
            return same_length and same_start and same_step
        except TypeError:
            return value == self
    
    def __len__(self):
        length = (self.stop - self.start) / self.step
        if length < 0:
            return 0
        if length % 1 > 0:
            return int(length) + 1
        return int(length)

    def __iter__(self):
        for x in range(len(self)):
            yield self.get_element(x)

    def __next__(self):
        current = self.current
        if self.pos and (current < self.stop):
            self.current += self.step
            return current
        if (not self.pos) and (current > self.stop):
            self.current += self.step
            return current
        raise StopIteration


if __name__ == "__main__":
    TEST = len(float_range(10))
    print(TEST)

    TEST = len(float_range(1, 11, -10))
    print(TEST)

    print(len(float_range(5, 0, -1)))
    
    TEST = list(float_range(5, 0, -1))
    print(TEST)
