from src.validation import Number

import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Data:
    """ Individual instance of the data, such as a row.

    This class is designed to be subclassed where a subclass defines the columns and validators for the data.
    The validators check the data meets the necessary requirements.

    Attributes:
        _columns: Dictionary where we define the columns and validators.
    """
    _columns = {}

    def __init__(self, **kwargs):
        """Initializes the data object and ensures the data meets the validators specified in the columns (kwargs)"""
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
        """Returns the columns specified for the data object."""
        return self._columns.keys()

    def to_dict(self):
        """Returns a dictionary with keys being column names and the values as the row items."""
        return {column: self.__dict__[column] for column in self._columns}


class DataContainer:
    """ Class that holds all data instances in a single object, allowing for manipulation of all data combined.

    This takes the type of row specified and only allows that type of data object. This ensures the data container only
    represents the defined data set.

    Attributes:
        _type_of_row: the type_of_row defines the type of data that will be allowed.
    """
    _type_of_row = Data
    data = []

    def __init__(self, data: list[Data]):
        """ Inits data, asserts the data is of _type_of_row specified by DataContainer.

        Raises:
            TypeError: Error when the data initialized is the wrong type."""
        for row in data:
            if not isinstance(row, self._type_of_row):
                raise TypeError()
            self.data.append(row)

    @property
    def _columns(self):
        """Returns columns allowed in the specified data object."""
        return self._type_of_row.columns

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
