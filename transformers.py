import datetime as dt
from time import strptime
from dateutil.parser import parse
from re import sub

def date_normalizer(date_input):

    supported_types = [dt.datetime, dt.date, str, int]

    if type(date_input) not in supported_types:
        raise TypeError(f"Date format {type(date_input)} not in supported formats: {supported_types}")
    elif type(date_input) == dt.datetime:
        return date_input.date()
    elif type(date_input) == str: 
        return parse(date_input).date()
    elif type(date_input) == int:
        return dt.date.fromtimestamp(date_input / 1e3)
    elif type(date_input) == dt.date:
        return date_input


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

def unit_converter(value, numerator_conversion, denominator_conversion)
    """unit_converter
    Convert a number into a specified unit type from a specified unit type.
    
    Args:
        value: (int, float) to be converted
        Unit_from: string of the units the data is currently in.
        Units_to: string of the desired units.
    
    Returns:
        Number that has had unit conversion. For example:
        10 [m3/s] = 10000/60 [l/min]
        """

#Creating conversion dictionary
conversion_dict = {("l","m3"): 1000,
            ("m3", "l"): 0.001,
            ("s", "min"): 1/60,
            ("min", "s"): 60,
            ("s", "hr"): 3600,
            ("hr", "s"): 1/3600,
            ("min", "hr"): 1/60,
            ("hr", "min"): 60,
            ("1","1"): 1}

# Need a way to look up the dictionary based on the function calls.
# How do you look up dictionary values.



    """
    1) Create a list with basic volume units [volume(L,m3)] Mass, time. 
    2) Create an logic flow (if diagram) to convert the units.
    3) Pass the function. 
    """