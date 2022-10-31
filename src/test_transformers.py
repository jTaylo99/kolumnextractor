import unittest

import transformers
import datetime as dt
from dateutil.parser import parse

class TestMain(unittest.TestCase):
    def test_transformers1(self):
        example_dates = [dt.datetime.now(),'6 Jan 2020', 1528797322 ,'2001/10/1']
        transformed_dates = [transformers.date_normalizer(a) for a in example_dates]
        assert transformed_dates == [dt.date.today(),dt.date(2020,1,6), dt.date(2018,6,12), dt.date(2001,10,1)]

    def test_transformers2(self):
        example_strings = ['this is-a string @swell & so is th1s']
        transformed_strings = [transformers.normalise(a) for a in example_strings]
        assert transformed_strings == ['thisisastringswellsoisth1s']

    def test_transformers3(self):    
        example_conversions = [[3, 'min', 's'],[2, 't','kg', 'l','m3'],]
        converted_values = [transformers.unit_converter(*a) for a in example_conversions]
        assert converted_values == [180,2000000]


if __name__ == '__main__':
    unittest.main()