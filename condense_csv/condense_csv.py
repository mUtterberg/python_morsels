def condense_csv(in_stream: str, *, id_name: str = None) -> str:
    """Group CSV text by the first column"""

    details = {}

    if id_name is None:
        header, in_stream = in_stream.split('\n', 1)
        header = header.split(',')
        id_name = header[0]

    line_attrs = [id_name]

    for line in in_stream.split('\n'):
        line_id, line_attr, line_value = line.split(',')
        details.setdefault(line_id, {})
        details[line_id][line_attr] = line_value
        if line_attr not in line_attrs:
            line_attrs.append(line_attr)

    out_rows = [line_attrs]
    for line_id in details:
        out_rows.append([line_id]+[details[line_id].get(line_attr, '') for line_attr in line_attrs[1:]])

    return '\n'.join(','.join(out_row) for out_row in out_rows)


def run_example():
    """Try something"""
    sample = '''01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29'''
    print(condense_csv(sample, id_name='Track'))
    print()
    text = """object,property,value
ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none"""
    print(condense_csv(text))


if __name__ == '__main__':
    run_example()
