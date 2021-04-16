from typing import Any, Dict


def flatten_dict(in_obj: Dict[str, Any], *, sep: str = '_') -> Dict[str, Any]:
    """Flattens a dict of dicts"""

    out_dict = {}
    for key, obj in in_obj.items():

        try:
            for inner_key, value in obj.items():
                out_dict[f'{key}{sep}{inner_key}'] = value
        except AttributeError:
            out_dict[key] = obj

    return out_dict


def run_examples() -> None:
    """Run examples"""
    print(flatten_dict({'vowels': {'a': 1, 'e': 2}, 'b': 4}))


if __name__ == '__main__':
    run_examples()
