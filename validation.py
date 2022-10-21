import logging
import datetime as dt

from abc import ABC, abstractmethod
from re import sub
from inflection import camelize

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def normalise(string):
    """
        normalise

    Converts a string into a normalised string. This removes all non-letter
    non-number characters from the string.

    Args:
        string: the string to be normalised

    Returns:
        A normalised string (only the letter & number characters). For example:
        this is-a string @swell & so is th1s => thisisastringswellsoisths
    """
    return sub(r"[\W_]+", "", string)


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


class String(Validator):
    def __init__(self, case=None):
        self.case = case

    def validate(self, value):
        if not isinstance(value, (str)):
            msg = f"Expected {value!r} to be a String"
            logging.error(msg)
            raise TypeError(msg)
        match self.case:
            case "lower":
                if value.lower() != value:
                    msg = f"Expected {value!r} to be all lower case."
                    logging.error(msg)
                    raise TypeError(msg)
            case "upper":
                if value.upper() != value:
                    msg = f"Expected {value!r} to be all upper case."
                    logging.error(msg)
                    raise TypeError(msg)
            case "camel":
                if camelize(value, False) != value:
                    msg = f"Expected {value!r} to be camel case."
                    logging.error(msg)
                    raise TypeError(msg)
            case "normalised":
                if normalise(value) != value:
                    msg = f"Expected {value!r} to be a normalised string."
                    logging.error(msg)
                    raise TypeError(msg)

class Date(Validator):
    def __init__(self, earliest_date=None, latest_date=None, first_of_month=False):
        self.earliest_date = earliest_date
        self.latest_date = latest_date
        self.first_of_month = first_of_month

    def validate(self, value):
        if not isinstance(value, (dt.date)):
            msg = f'Expected {value!r} to be an int or float'
            logging.error(msg)
            raise TypeError(msg)
        if self.earliest_date is not None and value < self.earliest_date:
            msg = f'Expected {value!r} to be at least {self.earliest_date!r}'
            logging.error(msg)
            raise ValueError(msg)
        if self.latest_date is not None and value > self.latest_date:
            msg = f'Expected {value!r} to be no more than {self.latest_date!r}'
            logging.error(msg)
            raise ValueError(msg)
        if self.first_of_month and value.day != 1:
            msg = f'Expected {value!r} to be first day of the month'
            logging.error(msg)
            raise ValueError(msg)
            