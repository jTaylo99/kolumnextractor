import csv
import os
import logging

from data_holder import Data

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def filter_columns(raw_data: list, columns_to_filter):
    logging.debug(f'Checking {raw_data = }\nand filtering based on {columns_to_filter}')
    index_to_keep = [raw_data[0].index(column) for column in columns_to_filter]
    logging.debug(f'{index_to_keep = }')
    return [[row[index] for index in index_to_keep] for row in raw_data]


def read_csv(info_dict):
    with open(info_dict["path"], newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        all_items = list(reader)
        if info_dict["columns"] is not None:
            all_items = filter_columns(all_items, columns_to_filter=info_dict["columns"])
        logging.debug(f'{all_items = }')
        return all_items


def determine_read(info_dict):
    match info_dict["type"]:
        case ".csv":
            return read_csv(info_dict)
        case other:
            logging.error('File is not a CSV. Please supply a CSV file type.')


def reading(filepath: str, columns):
    return determine_read({
        "path": filepath,
        "definition": columns,
        "type": os.path.splitext(filepath)[1],
        })


if __name__ == '__main__':
    test = reading(filepath="test.csv", columns=['column 1', 'column 2'])
    print(test)
