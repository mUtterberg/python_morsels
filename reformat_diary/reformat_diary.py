import datetime
# import re
from io import StringIO
from pathlib import Path
from typing import IO, List, Tuple


def clean_html(in_text: str) -> str:
    """Clean set HTML escape entities"""
    return in_text.strip().replace('&nbsp;', ' ').replace('&quot;', '\"').replace('&amp;', '&')


def entries_by_date(in_stream: IO) -> List[Tuple[str, str]]:
    """Formats a diary text file as tuples containing the date & diary entry"""

    entries = []
    this_entry = ['', '']  # type: List[str]
    all_lines = in_stream.readlines()
    n_lines = len(all_lines)
    this_line = 0
    while this_line < n_lines:
        line = all_lines[this_line]
        try:
            datetime.datetime.strptime(line[:-1], '%Y-%m-%d')
            if this_entry != ['', '']:
                this_entry[-1] = clean_html(this_entry[-1])
                entries.append(tuple(this_entry))
            this_entry = [line[:-1], '']
            this_line += 2
        except ValueError:
            this_entry[1] += line
            this_line += 1
    this_entry[-1] = clean_html(this_entry[-1])
    entries.append(tuple(this_entry))
    # in_text = in_stream.read()
    # date_text = re.compile(r'')

    return entries


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
