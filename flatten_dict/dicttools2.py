from typing import Any, Dict


def flatten_dict(in_obj: Dict[str, Any], *, sep: str = '_') -> Dict[str, Any]:
    """Flattens a dict of dicts"""

    out_dict = {}
    for key, obj in in_obj.items():

        try:
            for inner_key, value in obj.items():
                try:
                    out_dict.update(
                        flatten_dict(
                            {sep.join([str(key), str(inner_key)]): value}, sep=sep)
                        )
                except AttributeError:
                    out_dict[sep.join([key, inner_key])] = value
        except AttributeError:
            out_dict[key] = obj

    return out_dict


def run_examples() -> None:
    """Run examples"""
    print(flatten_dict({'vowels': {'a': 1, 'e': 2}, 'b': 4}))

    stuff = {'red': {'fruit': {'apple': 4}}, 'green': {'fruit': {'grape': 8}}}
    print(flatten_dict(stuff, sep='/'))


if __name__ == '__main__':
    run_examples()
