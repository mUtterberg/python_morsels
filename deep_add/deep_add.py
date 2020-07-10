

def deep_add(nested_list, start: int = 0):
    if hasattr(nested_list, '__iter__'):
        total = start
        for elem in nested_list:
            total = deep_add(elem, total)
        return total
    return nested_list + start


if __name__ == "__main__":
    NUMBERS = [1, 2, 3, 4]
    print(deep_add(NUMBERS, 1))
    print(deep_add(NUMBERS, 1))
