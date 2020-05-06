import argparse
import csv


parser = argparse.ArgumentParser()
parser.add_argument('in_csv')
parser.add_argument('out_csv')
parser.add_argument('--in-delimiter', dest="delim")
parser.add_argument('--in-quote', dest="quote")


def main(args):
    arguments = {}
    if args.delim:
        arguments['delimiter'] = args.delim
    if args.quote:
        arguments['quotechar'] = args.quote
    with open(args.in_csv, 'r', newline='') as in_file:

        # in_reader = csv.reader(in_file, delimiter=in_delim, quotechar=in_quote)

        if not (args.delim or args.quote):
            arguments['dialect'] = csv.Sniffer().sniff(in_file.read())
            in_file.seek(0)

        in_reader = csv.reader(in_file, **arguments)
        in_lines = list(in_reader)

    with open(args.out_csv, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(in_lines)


if __name__ == "__main__":
    cli_args = parser.parse_args()
    main(cli_args)
