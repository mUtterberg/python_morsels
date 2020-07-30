import csv


def csv_columns(file_object, headers=None, missing=None):
    csv_reader = csv.DictReader(file_object, fieldnames=headers, restval=missing)
    csv_dict = {name: [] for name in csv_reader.fieldnames}
    for row in csv_reader:
        for name in csv_reader.fieldnames:
            csv_dict[name].append(row[name])
    return csv_dict


if __name__ == "__main__":
    pass
