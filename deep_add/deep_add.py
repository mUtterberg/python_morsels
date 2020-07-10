

def is_int(input_elem):
    if isinstance(input_elem, int):
        return input_elem
    return


def has_value(input_elem):
    if not input_elem:
        return None
    return input_elem


def add_static(nested_list, output_sum):
    next_elem = nested_list.pop()
    try:
        output_sum += next_elem
    except TypeError as type_e:
        if 'NoneType' in type_e.args[0]:
            raise type_e
        try:
            nested_list += next_elem
        except TypeError:
            nested_list += list(next_elem)
    return output_sum


def deep_add(nested_list, start: int = 0):
    output_sum = start
    working_list = list(nested_list)
    while working_list:
        next_elem = working_list.pop()
        try:
            output_sum += next_elem
        except TypeError as type_e:
            if 'NoneType' in type_e.args[0]:
                raise type_e
            try:
                working_list += next_elem
            except TypeError:
                working_list += list(next_elem)
    return output_sum


if __name__ == "__main__":
    NUMBERS = [1, 2, 3, 4]
    print(deep_add(NUMBERS, 1))
    print(deep_add(NUMBERS, 1))
