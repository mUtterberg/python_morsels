import csv
from argparse import ArgumentParser, FileType
import sys
from typing import Any, IO, List, Tuple


def sort_multiple(row: List[str], indices: Tuple[str]) -> Tuple[Any, ...]:
    """Helper function to sort by multiple indices"""

    return_vals = []
    for i in indices:
        try:
            return_vals.append(row[int(i)])
        except ValueError:
            index, cli_type = i.split(':')
            value = row[int(index)]
            if cli_type == 'str':
                return_vals.append(value)
            elif cli_type == 'num':
                return_vals.append(int(value))
            else:
                raise TypeError()
    return tuple(return_vals)


def sort_by_column(file: IO, index_args: Tuple[str], with_header: bool = False) -> None:
    """Reads a CSV file, sorts it by a given column, prints the sorted rows"""

    reader = csv.reader(file)

    writer = csv.writer(sys.stdout)
    if with_header:
        writer.writerow(next(reader))

    for row in sorted(reader, key=lambda x: sort_multiple(x, index_args)):
        writer.writerow(row)

    file.close()


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('fname', type=FileType('r'))
    parser.add_argument('index', nargs='*')
    parser.add_argument('--with-header', action='store_true')

    cli_args, rem = parser.parse_known_intermixed_args()

    sort_by_column(cli_args.fname, cli_args.index, cli_args.with_header)
