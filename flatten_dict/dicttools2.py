from typing import Any, Callable, Dict, Iterable


def flatten_keys(in_keys):
    """Recursive helper function to flatten keys for key_maker"""
    return_keys = []
    if isinstance(in_keys, str):
        return [in_keys]
    if isinstance(in_keys, Iterable):
        for key in in_keys:
            if isinstance(key, Iterable):
                return_keys += flatten_keys(key)
            else:
                return_keys.append(key)
    else:
        return_keys.append(in_keys)
    return return_keys


def flatten_dict(in_obj: Dict[Any, Any], *, sep: str = '_', key_maker: Callable = None) -> Dict[str, Any]:
    """Flattens a dict of dicts"""

    if key_maker is None:
        key_maker = sep.join
    out_dict = {}
    for key, obj in in_obj.items():

        try:

            for inner_key, value in obj.items():
                try:

                    out_dict.update(
                        flatten_dict(
                            {(key, inner_key): value},
                            sep=sep,
                            key_maker=key_maker
                        )
                    )

                except AttributeError:
                    out_dict[key_maker(flatten_keys([key, inner_key]))] = value

        except AttributeError:
            out_dict[key_maker(flatten_keys(key))] = obj

    return out_dict


def run_examples() -> None:
    """Run examples"""
    # print(flatten_dict({'vowels': {'a': 1, 'e': 2}, 'b': 4}))

    stuff = {'red': {'fruit': {'apple': 4}}, 'green': {'fruit': {'grape': 8}}}
    # print(flatten_dict(stuff, sep='/'))
    weird_dict = flatten_dict(stuff, key_maker=tuple)
    print(weird_dict)

    print()
    weird_key = ((1, 2), 3)
    # print(list(flatten_keys(weird_key)))
    for key in weird_dict:
        print(list(flatten_keys(key)))


if __name__ == '__main__':
    run_examples()
