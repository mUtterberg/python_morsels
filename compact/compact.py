

def compact(in_seq):
    print(f"Compact received sequence of type {type(in_seq)}")
    current = object()
    in_seq = iter(in_seq)
    for coming in in_seq:
        if coming != current:
            current = coming
            yield current

if __name__ == "__main__":
    print("\nTesting compact([1, 1, 2, 1])")
    print(list(compact([1, 1, 2, 1])), '\n')
    print("\nTesting compact([1, 1, 2, 2, 3, 2])")
    print(list(compact([1, 1, 2, 2, 3, 2])), '\n')
    print("\nTesting compact(n**2 for n in [1, 2, 2, 3, 4])")
    print(list(compact(n**2 for n in [1, 2, 2, 3, 4])), '\n')
    print("\nTesting compact(n**2 for n in [1, 2, 2])")
    print(list(compact(n**2 for n in [1, 2, 2])), '\n')
