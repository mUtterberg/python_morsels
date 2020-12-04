from typing import Any, Dict, Tuple


SENTINEL = object()


def pluck(
        nested_dict: Dict[Any, Dict[Any, Any]],
        *key_paths: Tuple[str],
        sep: str = '.',
        default: Any = SENTINEL
    ) -> Any:
    """A helper for working with nested dict-based data"""

    if len(key_paths) > 1:
        return tuple(
            pluck(nested_dict, keys, sep=sep, default=default) for keys in key_paths
        )

    try:
        keys = key_paths[0].split(sep)
    except IndexError:
        raise ValueError(f'Missing positional argument "key_path(s)"')

    working_val = nested_dict.copy()

    for key in keys:
        try:
            working_val = working_val[key]
        except KeyError as key_e:
            if default != SENTINEL:
                return default
            raise key_e

    return working_val


if __name__ == "__main__":
    data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
    print(pluck(data, 'amount'))
    print(pluck(data, 'category.group'))
    print(pluck(data, 'category.created', default='N/A'))
    print(pluck(data, 'category.name', 'amount'))
