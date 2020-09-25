from itertools import zip_longest


def interleave(*iterables):
    """Zip input iterables"""

    sentinel = object()
    for items in zip_longest(*iterables, fillvalue=sentinel):
        for item in items:
            if item is not sentinel:
                yield item


if __name__ == "__main__":
    print(list(interleave([1, 2], [3,], [4, 5, 6])))
