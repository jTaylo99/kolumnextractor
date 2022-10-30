from src.validation import Number

import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Data:
    _columns = {}

    def __init__(self, **kwargs):
        if len(kwargs) != len(self._columns):
            msg = f'Expected {len(self._columns)} arguments.'
            logging.error(msg)
            raise TypeError(msg)

        for (column, validator) in self._columns.items():
            if validator is None:
                setattr(self, column, kwargs[column])
            else:
                validator.set_name(column)
                validator.__set__(self, kwargs[column])

    @property
    def columns(self):
        return self._columns

    def to_dict(self):
        """Returns a dictionary with keys being column names and the values as the row items."""
        return {column: self.__dict__[column] for column in self._columns}


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
        return self._type_of_row.columns

    def validate_row(self, row: Data):
        if list(row.__dict__.keys()) != self._columns:
            raise TypeError

    def all_data_to_dict(self):
        """Returns all data within the data container in the form of a list holding dictionaries."""
        to_return = []
        for data in self.data:
            to_return.append(data.to_dict())
        return to_return


if __name__ == '__main__':
    class Name(Data):
        _columns = {
            "Column 1": Number(minvalue=1, maxvalue=100),
            "Column 2": Number(minvalue=1, maxvalue=100),
            "Column 3": Number(minvalue=1, maxvalue=100),
        }

    class NameContainer(DataContainer):
        _type_of_row = Name
    name_row = Name(**{"Column 1":1, "Column 2":1, "Column 3":1})
    name_row2 = Name(**{"Column 1":68, "Column 2":66, "Column 3":24})
    container = NameContainer([name_row, name_row2])
    print(container.all_data_to_dict())
