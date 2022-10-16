from abc import ABC, abstractmethod
from re import sub


'''
    camel_case

Function to convert a string into a camel case style string. This removes spaces,
-, and _. And formats the capitals of the words into camel case. E.g.

    foo-bar => fooBar
    foo bar => fooBar
    Foo_Bar => fooBar
'''
def camel_case(string):
    string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
    return ''.join([string[0].lower(), string[1:]])


'''
    normalise

Function to convert a string into a normalised string. This removes all non-letter
non-number characters from the string. E.g.

this is-a string @swell & so is th1s => this isa string swell  so is ths

'''
def normalise(string):
    return sub(r"[^a-z0-9]", "", string.lower())


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
        if not isinstance(value, String):
            raise TypeError(f"Expected {value!r} to be a String")
        match self.case:
            case "lower":
                if value.lower() != value:
                    raise ValueError(f"Expected {value!r} to be all lower case.")
            case "upper":
                if value.upper() != value:
                    raise ValueError(f"Expected {value!r} to be all upper case.")
            case "camel":
                if camel_case(value) != value:
                    raise ValueError(f"Expected {value!r} to be camel case.")
            case "normalised":
                if normalise(value) != value:
                    raise ValueError(f"Expected {value!r} to be a normalised string.")
