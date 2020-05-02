

def add(*matrices):
    if len(set(len(matrix) for matrix in matrices)) != 1:
        raise ValueError('Given matrices are not the same size.')
    for rows in zip(*matrices):
        if len(set(len(row) for row in rows)) != 1:
            print('len(set(len(row) for row in rows)) returns', set(len(row) for row in rows))
            raise ValueError('Given matrices are not the same size.')
    return [
        [sum(vals) for vals in zip(*rows)]
        for rows in zip(*matrices)
    ]


if __name__ == "__main__":
    MATRIX_1 = [[1, -2], [-3, 4]]
    MATRIX_2 = [[2, -1], [0, -1]]
    print(f"Testing {MATRIX_1} + {MATRIX_2}")
    print(add(MATRIX_1, MATRIX_2), '\n')

    MATRIX_1 = [[1, 2, 3], [4, 5, 6]]
    MATRIX_2 = [[-1, -2, -3], [-4, -5, -6]]
    print(f"Testing {MATRIX_1} + {MATRIX_2}")
    print(add(MATRIX_1, MATRIX_2), '\n')

    m1 = [[6, 6], [3, 1]]
    m2 = [[1, 2], [3, 4]]
    m3 = [[2, 1], [3, 4]]
    m4 = [[9, 9], [9, 9]]
    m5 = [[31, 32], [27, 24]]

    print(f"Testing {m1} + {m2} + {m3}")
    print(add(m1, m2, m3), '\n')

    print(f"Testing {m1} + {m2} + {m3} + {m4} + {m5}")
    print(add(m1, m2, m3, m4, m5), '\n')

    MATRIX_1 = [[], []]
    MATRIX_2 = [[], []]
    print(f"Testing {MATRIX_1} + {MATRIX_2}")
    print(add(MATRIX_1, MATRIX_2), '\n')

    m1 = [[6, 6], [3, 1]]
    m2 = [[1, 2], [3, 4], [5, 6]]
    m3 = [[6, 6], [3, 1, 2]]
    print(f"Testing mismatch (extra row SHOULD RAISE)")
    print(add(m1, m2), '\n')

    print(f"Testing mismatch (extra column SHOULD RAISE)")
    print(add(m1, m2, m3), '\n')
