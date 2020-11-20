import argparse
import csv
from pathlib import Path
from typing import IO, Any, List, Tuple, Union


def parse_fixed_width_file(in_stream: IO, start_end: List[Tuple[int, ...]]) -> List[List[Any]]:
    """Turn fixed-width file into a CSV file"""

    rows = in_stream.readlines()

    return [
        [
            row[slice(*slicer)].strip()
            for slicer in start_end
        ]
        for row in rows
    ]


def parse_columns(column_pairs: str) -> List[Tuple[int, ...]]:
    """Detect start_end from string format"""
    return [
        tuple(int(x) for x in pair.split(':'))
        for pair in column_pairs.split(',')
    ]


def main(cli_args: Union[argparse.Namespace, List[str]]) -> None:
    """Write CSV based on arguments"""

    txt_file = None
    if isinstance(cli_args, argparse.Namespace):
        cols = cli_args.cols
        txt_file = cli_args.txt_file
        csv_file = cli_args.csv_file
    else:
        for arg in cli_args:
            if arg.startswith('--cols='):
                cols = arg[7:]
            elif txt_file is None:
                txt_file = arg
            else:
                csv_file = arg

    start_end = parse_columns(cols)
    with open(txt_file, 'r') as in_stream:
        file_data = parse_fixed_width_file(in_stream, start_end)

    out_file = Path(csv_file)
    out_file.touch(exist_ok=True)
    with out_file.open('w') as out_stream:
        writer = csv.writer(out_stream)
        writer.writerows(file_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('txt_file', type=str)
    parser.add_argument('csv_file', type=str)
    parser.add_argument('--cols', type=str, required=True)
    arguments, _ = parser.parse_known_args()
    main(arguments)
