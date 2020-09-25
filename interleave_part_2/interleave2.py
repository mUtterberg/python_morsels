from itertools import zip_longest


def interleave(*iterables):
    """Zip input iterables"""

    sentinel = object()
    for items in zip_longest(*iterables, fillvalue=sentinel):
        for item in items:
            if item is not sentinel:
                yield item

# def interleave(*iterables):
#     """Iterate over input iterables"""

#     iterators = [iter(i) for i in iterables]
#     while iterators:
#         for iterator in list(iterators):
#             try:
#                 yield next(iterator)
#             except StopIteration:
#                 iterators.remove(iterator)


if __name__ == "__main__":
    print(list(interleave([1, 2], [3,], [4, 5, 6])))
