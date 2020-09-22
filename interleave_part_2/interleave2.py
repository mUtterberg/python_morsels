from itertools import zip_longest


def interleave(*iterables):
    """Zip input iterables"""

    for items in zip_longest(*iterables, fillvalue='OBSCURE_FILLED_CONST'):
        for item in items:
            if item != 'OBSCURE_FILLED_CONST':
                yield item


if __name__ == "__main__":
    print(list(interleave([1, 2], [3,], [4, 5, 6])))
