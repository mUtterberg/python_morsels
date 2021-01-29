from operator import length_hint


def total_length(*args, use_hints: bool = False) -> int:
    """Add lengths"""
    ret_val = 0
    for arg in args:
        try:
            ret_val += len(arg)
        except TypeError:
            if use_hints:
                hint = length_hint(arg)
                if hint > 0:
                    ret_val += hint
                else:
                    for _ in arg:
                        ret_val += 1
            else:
                for _ in arg:
                    ret_val += 1
    return ret_val
