import argparse
import csv


parser = argparse.ArgumentParser()
parser.add_argument('in_csv')
parser.add_argument('out_csv')


def main(in_csv, out_csv):
    with open(in_csv, 'r') as in_file:
        # reader = csv.reader(in_file)
        in_lines = in_file.readlines()

    in_lines = [
        [element for element in row[:-1].split('|')]
        for row in in_lines
    ]

    with open(out_csv, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(in_lines)


if __name__ == "__main__":
    cli_args = parser.parse_args()
    main(cli_args.in_csv, cli_args.out_csv)
