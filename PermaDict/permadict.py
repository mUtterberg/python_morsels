from collections import UserDict


SENTINEL = object()


class PermaDict(UserDict):
    """A class has no function."""

    def __setitem__(self, key, item) -> None:
        if super().get(key, SENTINEL) is SENTINEL:
            return super().__setitem__(key, item)
        raise KeyError(f'\'{key}\' already in dictionary')


def check_cases():
    """Review cases from exercises"""
    perma_dict = PermaDict({'Trey': "San Diego", 'Al': "San Francisco"})
    print(perma_dict)


if __name__ == '__main__':
    check_cases()
