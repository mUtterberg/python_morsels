from collections import UserDict
from typing import Mapping, Optional


SENTINEL = object()


class PermaDict(UserDict):
    """A class has no function."""

    def __init__(self, __dict: Optional[Mapping] = None, **kwargs) -> None:
        data = dict(kwargs)

        self.silent = data.pop('silent', False)

        if __dict is None:
            super().__init__(data)
        else:
            super().__init__(__dict)

    def __setitem__(self, key, item, force: bool = False) -> None:
        if force or super().get(key, SENTINEL) is SENTINEL:
            return super().__setitem__(key, item)
        if self.silent:
            return None
        raise KeyError(f'\'{key}\' already in dictionary')

    def update(self, other=None, **kwargs):

        force = kwargs.pop('force', False)

        if other is None:
            data = kwargs
        else:
            data = dict(other)

        for key, value in data.items():
            self.__setitem__(key, value, force)

    def force_set(self, key, value) -> None:
        """Force mutability of existing key-values"""
        return super().__setitem__(key, value)


def check_cases():
    """Review cases from exercises"""
    perma_dict = PermaDict({'Trey': "San Diego", 'Al': "San Francisco"})
    print(perma_dict)


if __name__ == '__main__':
    check_cases()
