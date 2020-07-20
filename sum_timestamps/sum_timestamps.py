import datetime
from typing import List


def sum_timestamps(list_of_timestamps: List[str]) -> str:
    all_times = [in_time.rsplit(':') for in_time in list_of_timestamps]
    out_time = datetime.timedelta(0, 0, 0)
    for split_time in all_times:
        out_time += datetime.timedelta(seconds=int(split_time[-1]), minutes=int(split_time[-2]))
        try:
            out_time += datetime.timedelta(hours=int(split_time[-3]))
        except IndexError:
            continue
    print(out_time)
    out_hours = out_time.days * 24 + out_time.seconds//3600
    out_minutes = out_time.seconds // 60 % 60
    out_seconds = out_time.seconds % 60
    out_time = ''
    hours = False
    if out_hours > 0:
        out_time += f'{out_hours}:'
        hours = True
    if hours:
        out_time += f'{out_minutes:02}:'
    else:
        out_time += f'{out_minutes}:'
    out_time += f'{out_seconds:02}'
    return out_time


if __name__ == "__main__":
    print(sum_timestamps(['12:31', '15:13', '17:59']))
