from typing import Iterable, Iterator


def deep_flatten(flatten_me: Iterable) -> Iterator:
    """Flatten an iterable"""

    for item in flatten_me:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            for inner in deep_flatten(item):
                yield inner
        else:
            yield item


if __name__ == "__main__":
    print(next(iter([2, 1])))

    DEMO = [0, [1, [2, 3]], [4]]
    print(list(deep_flatten(DEMO)))

    print()
    NUM_WORDS = enumerate([99, 98, 97])
    FLAT = deep_flatten(NUM_WORDS)
    print(next(FLAT))
    print(next(FLAT))
    print(next(NUM_WORDS))
