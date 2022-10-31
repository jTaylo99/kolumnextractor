import logging
import datetime as dt

from abc import ABC, abstractmethod
from inflection import camelize

from src.transformers import normalise

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def to_number(str):
    """
        to_number(str)

    Converts string from input into a number.

    Args:
        str: the string to be converted

    Returns:
        The string as an Int if it is an Int, a Float if it is a Float, 
        or returns a ValueError if it is neither.
    """
    try:
        return int(str)
    except ValueError:
        try:
            return float(str)
        except ValueError:
            return ValueError


class Validator(ABC):
    def __init__(self):
        self.name = None

    def set_name(self, name):
        """Takes a name and converts it to a string. This is the attribute of the class."""
        self.name = f'{name}'

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        """Validates the value given. If validation passes, it sets the attribute of the object given using self.name
        and the value.

        Args
            obj: Where the attribute is set, if validation passes.
            value: The value to be validated. If passed, this is set as attribute of the object."""
        self.validate(value)
        setattr(obj, self.name, value)

    @abstractmethod
    def validate(self, value):
        """A method meant to be over writen by subclasses, that provides the actual validation of values being
        passed."""
        pass


class Number(Validator):
    """
    A subclass of Validator that checks values are within the max and min range specified.

    Attributes:
        minvalue: Minimum value allowed for the data.
        maxvalue: Maximum value allowed for the data.
    """
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        """Takes a value and checks it's a number (int or float). If so, checks if it is within the specified max
        and min range.

        Args:
            value: Value to be validated.

        Raises:
            TypeError: If value is not an int or float.
        """
        if value == None or value == "":
            print(value)
            value = self.default
            return
        if not isinstance(value, (int, float)):
            value = to_number(value)
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
    """
    A subclass of Validator that checks if the data is a string and that it's case (capital, lower) matches the input.

    Attributes:
        case: The case to test the string input.
    """
    def __init__(self, case=None):
        self.case = case

    def validate(self, value):
        """ Validates the input is text and that it is in the desired case.

        Args:
            value: The data entry to be validated. String.

        Raises:
            TypeError: An error if the value is not a string or if it is in the wrong case.
        """
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
    """
    A subclass of Validator that checks if the data is a date and that it meets date requirements.

    Attributes:
        earliest_date: The earliest valid date.
        latest_date: The latest valid date.
        first_of_month: boolean to check if the data is the first of a month or not. Default is false.
    """
    def __init__(self, earliest_date=None, latest_date=None, first_of_month=False):
        self.earliest_date = earliest_date
        self.latest_date = latest_date
        self.first_of_month = first_of_month

    def validate(self, value):
        """Validates the date value is in date time format and within specified limits

        Args:
            value: the date to be validated.

        Raises:
            TypeError: An error if the value is not a date time date.
            ValueError: Error if the value exceeds the earliest date, the latest date or is not the first of the month.
        """
        if not isinstance(value, dt.date):
            msg = f'Expected {value} to be a dt.date'
            logging.error(msg)
            raise TypeError(msg)
        if self.earliest_date is not None and value < self.earliest_date:
            msg = f'Expected {value} to be at least {self.earliest_date!r}'
            logging.error(msg)
            raise ValueError(msg)
        if self.latest_date is not None and value > self.latest_date:
            msg = f'Expected {value} to be no more than {self.latest_date}'
            logging.error(msg)
            raise ValueError(msg)
        if self.first_of_month and value.day != 1:
            msg = f'Expected {value} to be first day of the month'
            logging.error(msg)
            raise ValueError(msg)
