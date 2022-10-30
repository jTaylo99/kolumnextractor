import datetime as dt
from src import config_parameters
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


def unit_converter(value, numerator_from, numerator_to, denominator_from=None, denominator_to=None):
    """
        unit_converter

    Convert a number into a specified unit type from a specified unit type.
    
    Args:
        value: (int, float) to be converted
        numerator_from: string that represents the numerator units the data is currently in.
        numerator_to: string of the desired numerator unit.
        denominator_from: (Optional) string of the denominator unit. By default, it is set to 1.
        denominator_to: (Optional) string of the denominator unit to be converted to. By default, it is set to 1.
    
    Returns:
        Number that has had unit conversion. For example:
        10 [m3/s] = 10000/60 [l/min]
    """
    try:
        if denominator_from is not None and denominator_to is not None:
            return config_parameters.conversion_dict[(numerator_from, numerator_to)] * value / \
                   (config_parameters.conversion_dict[(denominator_from, denominator_to)])
        else:
            return config_parameters.conversion_dict[(numerator_from, numerator_to)] * value
    except KeyError:
        raise KeyError(f"The units are not recognised. Check that both units are either of"
                       f" {set([item for sublist in config_parameters.conversion_dict.keys() for item in sublist])}"
                       f" and that you can convert between them")
