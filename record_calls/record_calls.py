from typing import Callable


class record_calls:
    """Record the number of times a function is called."""

    def __init__(self, func: Callable) -> None:
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)


# def record_calls(func) -> Callable:
#     """Record the number of times a function is called."""

#     def func_wrapper(*args, **kwargs):
#         try:
#             func_wrapper.call_count += 1
#         except AttributeError:
#             func_wrapper.call_count = 1
#         return func(*args, **kwargs)

#     if 'call_count' not in func_wrapper.__dict__:
#         func_wrapper.call_count = 0
#     return func_wrapper


@record_calls
def greet(name: str = 'world') -> None:
    """Greet name"""
    print(f'Hello {name}')


if __name__ == "__main__":
    print(greet.call_count)
    greet('Trey')
    print(greet.call_count)
    greet('Trey')
    print(greet.call_count)
    greet('Trey')
    print(greet.call_count)
