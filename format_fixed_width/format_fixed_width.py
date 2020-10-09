def format_fixed_width(rows, padding=2, widths=None, alignments=None) -> str:
    """Formats a list of lists as a fixed-width formatted string"""
    if not rows:
        return ''

    if widths is None:
        widths = [
            max(len(cell) for cell in col)
            for col in zip(*rows)
        ]

    if alignments is None:
        alignments = ['L' for col in zip(*rows)]

    pad = ' ' * padding
    return '\n'.join(
        [
            pad.join(
                [
                    item.rjust(widths[i], ' ')
                    if alignments[i] == 'R'
                    else item.ljust(widths[i], ' ')
                    for i, item in enumerate(row)
                ]
            ).rstrip() for row in rows
        ]
    )


if __name__ == "__main__":
    pass
