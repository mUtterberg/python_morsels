

def uniques_only(num_iter):
    try:
        current = hash(num_iter)
        return (
            x
            for x in dict.fromkeys(current)
        )
    except TypeError as type_e:
        nums_used = []
        for x in num_iter:
            if x not in nums_used:
                nums_used.append(x)
                yield x


if __name__ == "__main__":
    print(list(uniques_only([1, 4, 9, 16])))
    hashables = 'ababcde'
    print(list(uniques_only(hashables)))
