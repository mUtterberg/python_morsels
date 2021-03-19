import csv
from argparse import ArgumentParser, FileType
import sys
from typing import IO


def sort_by_column(file: IO, in_x: int) -> None:
    """Reads a CSV file, sorts it by a given column, prints the sorted rows"""

    reader = csv.reader(file)
    writer = csv.writer(sys.stdout)

    for row in sorted(reader, key=lambda x: x[in_x]):
        writer.writerow(row)

    file.close()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('fname', type=FileType('r'))
    parser.add_argument('index', type=int)
    cli_args = parser.parse_args()
    sort_by_column(cli_args.fname, cli_args.index)
