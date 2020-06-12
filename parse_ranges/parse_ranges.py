

def parse_ranges(in_str):
    ranges = in_str.split(',')
    for x in ranges:
        start_range = int(x.split('-')[0].strip())
        end_range = int(x.split('-')[-1].strip())+1
        for z in range(start_range,end_range):
            yield z
