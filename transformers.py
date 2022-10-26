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
        