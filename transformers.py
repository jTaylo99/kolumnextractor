import datetime as dt
from time import strptime
from dateutil.parser import parse

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
        