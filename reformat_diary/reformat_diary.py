import datetime
from io import StringIO
from pathlib import Path
from typing import IO, Iterator, Tuple


def clean_html(in_text: str) -> str:
    """Clean set HTML escape entities"""
    return in_text.strip().replace('&nbsp;', ' ').replace('&quot;', '\"').replace('&amp;', '&')


def entries_by_date(in_stream: IO) -> Iterator[Tuple[str, str]]:
    """Formats a diary text file as tuples containing the date & diary entry"""

    date = None
    entry = ''
    for line in in_stream:
        try:
            datetime.datetime.strptime(line.strip(), '%Y-%m-%d')
            if date:
                yield date, clean_html(entry)
            date, entry = line.strip(), ''
        except ValueError:
            entry += line
    if date is None:
        raise Exception('Diary is empty')
    yield date, clean_html(entry)


def main(f_name: str) -> None:
    """Accept diary filename & create files for each diary entry."""
    with Path(f_name).open('r') as in_stream:
        diary = entries_by_date(in_stream)
        for entry in diary:
            out_name, out_text = entry
            out_name = f'{out_name}.txt'
            with Path(out_name).open('w') as out_file:
                out_file.write(out_text)
                print(f'{out_name} written')


if __name__ == "__main__":
    print(entries_by_date(StringIO('this-is-not-a-date\n')))
    print(entries_by_date(StringIO("2018-01-01\n\nI created a Python exercise today.")))
