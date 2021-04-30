import argparse
import unicodedata
from typing import IO


def unsmarten(in_stream: IO) -> str:
    """Actual conversion function"""
    in_text = in_stream.read()
    in_stream.close()
    out_text = ''
    for cha in in_text:
        if 'DOUBLE QUOTATION' in unicodedata.name(cha, 'f'):
            out_text += '"'
        elif 'SINGLE QUOTATION' in unicodedata.name(cha, 'f'):
            out_text += '\''
        else:
            out_text += cha
    return out_text


def main():
    """Convert smart quotes to standard quotes"""
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r', encoding='utf-8', errors='strict'))
    cli_args = parser.parse_args()
    print(unsmarten(cli_args.file), end='')


if __name__ == '__main__':
    main()
