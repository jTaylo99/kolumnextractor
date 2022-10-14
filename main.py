import csv
import os


def filter_columns(raw_data: list, columns_to_filter):
    index_to_keep = [raw_data[0].index(column) for column in columns_to_filter]
    return [[row[index] for index in index_to_keep] for row in raw_data]


def read_csv(info_dict):
    with open(info_dict["path"], newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        all_items = list(reader)
        if info_dict["columns"] is not None:
            all_items = filter_columns(all_items, columns_to_filter=info_dict["columns"])
        return all_items


def determine_read(info_dict):
    match info_dict["type"]:
        case ".csv":
            return read_csv(info_dict)


def reading(filepath: str, columns):
    return determine_read({"path": filepath,
                           "columns": columns,
                           "type": os.path.splitext(filepath)[1]})

if __name__ == '__main__':
    test = reading(filepath="test.csv", columns=['column 1'])
