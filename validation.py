from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = f'_{name}'

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            msg = f'Expected {value!r} to be an int or float'
            logging.error(msg)
            raise TypeError(msg)
        if self.minvalue is not None and value < self.minvalue:
            msg = f'Expected {value!r} to be at least {self.minvalue!r}'
            logging.error(msg)
            raise ValueError(msg)
        if self.maxvalue is not None and value > self.maxvalue:
            msg = f'Expected {value!r} to be no more than {self.maxvalue!r}'
            logging.error(msg)
            raise ValueError(msg)