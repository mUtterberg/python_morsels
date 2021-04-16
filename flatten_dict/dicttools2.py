from typing import Any, Dict


def flatten_dict(in_obj: Dict[str, Dict[str, Any]], *, sep: str = '_') -> Dict[str, Any]:
    """Flattens a dict of dicts"""

    out_dict = {}
    for key, in_dict in in_obj.items():
        for in_key, value in in_dict.items():
            out_dict[f'{key}{sep}{in_key}'] = value

    return out_dict


if __name__ == '__main__':
    pass
