from dataclasses import dataclass
from functools import update_wrapper, wraps
from typing import Any, Callable, Optional


NO_RETURN = object()


@dataclass
class RecordCalls:
    """Dataclass for tracking args & kwargs"""
    __slots__ = ['args', 'kwargs', 'return_value', 'exception']
    args: Any
    kwargs: Any
    return_value: Optional[Any]
    exception: Optional[Exception]


# class record_calls:
#     """Record the number of times a function is called."""

#     def __init__(self, func: Callable) -> None:
#         self.func = func
#         # self._str = str(func)
#         self.call_count = 0
#         self.calls = []
#         update_wrapper(self, func)

#     # def __str__(self) -> str:
#     #     return self._str

#     def __call__(self, *args, **kwargs):

#         current_call = RecordCalls(args, kwargs, None, None)

#         try:
#             return_val = self.func(*args, **kwargs)
#         except Exception as bare_e:
#             current_call.exception = bare_e
#             return_val = NO_RETURN

#         current_call.return_value = return_val
#         self.calls.append(current_call)
#         self.call_count += 1

#         if current_call.exception:
#             raise current_call.exception

#         return return_val


def record_calls(func) -> Callable:
    """Record the number of times a function is called."""

    @wraps(func)
    def func_wrapper(*args, **kwargs):

        current_call = RecordCalls(args, kwargs, None, None)

        try:
            return_val = func(*args, **kwargs)

        except Exception as bare_e:
            return_val = NO_RETURN
            current_call.exception = bare_e

        current_call.return_value = return_val
        func_wrapper.calls.append(current_call)
        func_wrapper.call_count += 1
        if current_call.exception:
            raise current_call.exception
        return return_val

    if 'call_count' not in func_wrapper.__dict__:
        func_wrapper.call_count = 0
        func_wrapper.calls = []
    return func_wrapper


@record_calls
def greet(name: str = 'world') -> None:
    """Greet name"""
    print(f'Hello {name}')


def example(a, b=True):
    """Example function."""
    print('hello world')


if __name__ == "__main__":
    DECORATED = record_calls(example)
    print(str(example))
    print(str(DECORATED))

    print(greet)
    greet('Marissa')
    print(greet.call_count)
    print(greet.__name__)
