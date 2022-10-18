from abc import ABC, abstractmethod
from re import sub
from inflection import camelize


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
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f'Expected {value!r} to be at least {self.minvalue!r}'
            )
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f'Expected {value!r} to be no more than {self.maxvalue!r}'
            )


class String(Validator):
    def __init__(self, case=None):
        self.case = case

    def validate(self, value):
        if not isinstance(value, (str)):
            raise TypeError(f"Expected {value!r} to be a String")
        match self.case:
            case "lower":
                if value.lower() != value:
                    raise ValueError(f"Expected {value!r} to be all lower case.")
            case "upper":
                if value.upper() != value:
                    raise ValueError(f"Expected {value!r} to be all upper case.")
            case "camel":
                if camelize(value, False) != value:
                    raise ValueError(f"Expected {value!r} to be camel case.")
            case "normalised":
                if normalise(value) != value:
                    raise ValueError(f"Expected {value!r} to be a normalised string.")
