import validation

import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Data:
    _columns = {}

    def __init__(self, *args):
        if len(args) != len(self._columns):
            msg = f'Expected {len(self._columns)} arguments.'
            logging.error(msg)
            raise TypeError(msg)

        for (column, validator), value in zip(self._columns.items(), args):
            validator.set_name(column)
            validator.__set__(self, value)

    @property
    def columns(self):
        return self._columns


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


if __name__ == '__main__':
    class Name(Data):
        _columns = {
            "Column_1": validation.Unsigned(),
            "Column_2": validation.String(case='lower'),
            "Column_3": validation.Number(minvalue=1, maxvalue=100),
        }
    name_row = Name(100.0, 'lower', 1)
