

def parse_ranges(in_str):
    ranges = in_str.split(',')
    out_str = [z for x in ranges for z in range(int(x.split('-')[0].strip()),int(x.split('-')[1].strip())+1)]
    return out_str
