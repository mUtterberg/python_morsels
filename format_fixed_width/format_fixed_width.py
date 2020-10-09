def format_fixed_width(in_list, padding=2, widths=None) -> str:
    """Formats a list of lists as a fixed-width formatted string"""
    if not in_list:
        return ''

    if widths is None:
        widths = [
            max([len(nested_list[i]) for nested_list in in_list])
            for i in range(max([len(nested_list) for nested_list in in_list]))
        ]

    pad = ' ' * padding
    return '\n'.join(
        [
            pad.join(
                [
                    item.ljust(widths[i], ' ') for i, item in enumerate(nested_list)
                ]
            ).rstrip() for nested_list in in_list
        ]
    )


if __name__ == "__main__":
    pass