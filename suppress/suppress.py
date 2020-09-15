from typing import Any


class suppress:
    """Context manager to suppress exceptions of a given type"""
    def __init__(self, *args) -> Any:
        # print('Initializing with args:', args)
        self.suppress_types = args
        self.exception = None
        self.traceback = None
        self.function = None
        # print('Initialized')

    def __enter__(self):
        # print('Entering')
        return self

    def __exit__(self, exit_type, exit_value, exit_traceback):
        # print('Exiting')
        if isinstance(exit_value, self.suppress_types):
            self.exception = exit_value
            self.traceback = exit_traceback
            return self
        else:
            # self.suppress_types = None
            pass

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # print('Calling with args/kwargs:', args, kwds)
        if callable(args[0]):
            self.function = args[0]
            return self
        with self:
            return self.function(*args)


@suppress(TypeError)
def len_or_none(thing):
    """Mock suppress as decorator"""
    return len(thing)


if __name__ == "__main__":
    with suppress(NameError) as suppress_me:
        print('Is it working?')
        print('It\'s nice to meet you,', name)
        print('It IS working!')

    print(suppress_me.exception)

    print(len_or_none([1, 2, 3]))
    print(len_or_none(64))
