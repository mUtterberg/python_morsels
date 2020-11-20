import argparse
import csv
from argparse import FileType
from typing import IO, Generator, Iterable, List, Tuple


def parse_fixed_width_file(in_stream: IO, start_end: Iterable[Tuple[int, ...]]) -> Generator[List[str], None, None]:
    """Turn fixed-width file into a CSV file"""

    return (
        [
            row[slice(*slicer)].rstrip()
            for slicer in start_end
        ]
        for row in in_stream
    )


def parse_columns(column_pairs: str) -> List[Tuple[int, int]]:
    """Detect start_end from string format"""
    pairs = (
        pair.split(':')
        for pair in column_pairs.split(',')
    )
    return [
        (int(start), int(stop))
        for (start, stop) in pairs
        ]


def parse_args(cli_args: List[str]):
    """Parse CLI args"""
    parser = argparse.ArgumentParser()
    parser.add_argument('txt_file', type=FileType('rt'))
    parser.add_argument('csv_file', type=FileType('wt'))
    parser.add_argument('--cols', type=str, required=True)
    arguments, _ = parser.parse_known_args(cli_args)
    return arguments


def main(cli_args: List[str]) -> None:
    """Write CSV based on arguments"""

    if not isinstance(cli_args, argparse.Namespace):
        cli_args = parse_args(cli_args)

    cols = cli_args.cols
    txt_file = cli_args.txt_file
    csv_file = cli_args.csv_file

    start_end = parse_columns(cols)
    file_data = parse_fixed_width_file(txt_file, start_end)

    writer = csv.writer(csv_file)
    writer.writerows(file_data)


if __name__ == "__main__":
    pass
