import argparse
import unicodedata
from typing import IO


def unsmarten_line(in_line: str) -> str:
    """Single line"""
    out_text = ''
    for cha in in_line:
        if 'DOUBLE QUOTATION' in unicodedata.name(cha, 'f'):
            out_text += '"'
        elif 'SINGLE QUOTATION' in unicodedata.name(cha, 'f'):
            out_text += '\''
        elif 'ELLIPS' in unicodedata.name(cha, 'f'):
            out_text += '...'
        elif 'EN DASH' in unicodedata.name(cha, 'f'):
            out_text += '-'
        elif 'EM DASH' in unicodedata.name(cha, 'f'):
            out_text += '--'
        else:
            out_text += cha
    return out_text.rstrip() + '\n'


def unsmarten(in_stream: IO) -> str:
    """Actual conversion function"""
    in_text = in_stream.readlines()
    in_stream.close()
    out_text = ''
    for line in in_text:
        out_text += unsmarten_line(line)
    return out_text


def main():
    """Convert smart quotes to standard quotes"""
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r', encoding='utf-8', errors='strict'))
    cli_args = parser.parse_args()
    print(unsmarten(cli_args.file), end='')


if __name__ == '__main__':
    main()
