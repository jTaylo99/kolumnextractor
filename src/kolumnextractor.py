import csv
import os
import logging
from src.data_container import Data, DataContainer
from src.validation import Number, normalise

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def filter_columns(raw_data: list, columns_to_filter):
    logging.debug(f'Checking {raw_data = }\nand filtering based on {columns_to_filter}')
    index_to_keep = [raw_data[0].index(column) for column in columns_to_filter]
    logging.debug(f'{index_to_keep = }')
    return [[row[index] for index in index_to_keep] for row in raw_data]


def construct_datacontainer(raw_data: list, columns: Data):
    data = []
    for r in raw_data:
        print(r)
        row = {col: r[col] for col in columns._columns.keys()}
        data.append(columns(**row))
    return DataContainer(data)


def read_csv(info_dict):
    with open(info_dict["path"], newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        all_items = list(reader)
        headers = [normalise(h) for h in all_items.pop(0)]
        raw_data = [dict(zip(headers, r)) for r in all_items]
        if info_dict["columns"] is not None:
            data = construct_datacontainer(raw_data, info_dict["columns"])
            # all_items = filter_columns(all_items, columns_to_filter=info_dict["columns"])
        logging.debug(f'{data = }')
        return data


def determine_read(info_dict):
    match info_dict["type"]:
        case ".csv":
            return read_csv(info_dict)
        case other:
            logging.error('File is not a CSV. Please supply a CSV file type.')


def reading(filepath: str, columns):
    return determine_read({
        "path": filepath,
        "columns": columns,
        "type": os.path.splitext(filepath)[1],
        })


def reading_data(filepath: str, columns: Data):
    return determine_read({"path": filepath,
                           "columns": columns,
                           "type": os.path.splitext(filepath)[1]})


if __name__ == '__main__':
    class Name(Data):
        _columns = {"column2": Number(minvalue=1, maxvalue=100),
                    "column1": Number(minvalue=1, maxvalue=100),
                    "column3": Number(minvalue=1, maxvalue=100),}
    test = reading_data(filepath="../data/test.csv", columns=Name)
    print(test.data[0]._columns)
