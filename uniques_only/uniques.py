

def uniques_only(num_iter):
    seen_hashable = set()
    seen_unhashable = []
    for item in num_iter:
        try:
            if item not in seen_hashable:
                yield item
                seen_hashable.add(item)
        except TypeError:
            if item not in seen_unhashable:
                yield item
                seen_unhashable.append(item)


if __name__ == "__main__":
    print(list(uniques_only([1, 4, 9, 16])))
    hashables = 'ababcde'
    print(list(uniques_only(hashables)))
