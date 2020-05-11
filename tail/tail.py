import collections


def tail(in_list, last_n):
    if last_n > 0:
        out_deque = collections.deque(maxlen=last_n)
        for elem in in_list:
            out_deque.append(elem)
        return list(out_deque)
    return []


if __name__ == "__main__":
    IN_LIST = [1, 2, 3, 4, 5]
    LAST_N = 3
    print(tail(IN_LIST, LAST_N))

    IN_LIST = 'hello'
    LAST_N = 2
    print(tail(IN_LIST, LAST_N))

    IN_LIST = 'hello'
    LAST_N = 0
    print(tail(IN_LIST, LAST_N))

    NUMS = (n**2 for n in [1, 2, 3, 4])
    LAST_N = 2
    print(tail(NUMS, LAST_N))
