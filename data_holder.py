from validation import Number

import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Data:
    _columns = {}

    def __init__(self, **kwargs):
        if len(kwargs) != len(self._columns):
            msg = f'Expected {len(self._columns)} arguments.'
            logging.error(msg)
            raise TypeError(msg)

        for name, value in zip(self._columns.keys(), kwargs):
            setattr(self, name, value)


class DataContainer:
    _type_of_row = Data
    data = []

    def __init__(self, data: list[Data]):
        for row in data:
            if not isinstance(row, self._type_of_row):
                raise TypeError()
            self.data.append(row)

    @property
    def _columns(self):
        return self._type_of_row._columns

    def validate_row(self, row: Data):
        if list(row.__dict__.keys()) != self._columns:
            raise TypeError


class Name(Data):
    _columns = {"Column 1": Number(minvalue=1, maxvalue=100),
                "Column 2": Number(minvalue=1, maxvalue=100),
                "Column 3": Number(minvalue=1, maxvalue=100),}


class Name2(Data):
    _columns = ["Column 4", "Column 5", 'Column 6']


class NameHolder(DataContainer):
    _type_of_row = Name
