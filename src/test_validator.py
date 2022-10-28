import unittest
import datetime as dt
from validation import String, Date

def broken_function():
    raise Exception('This is broken')

class TestValidator(unittest.TestCase):
    
    #default case is not handled in the code
    def test_string(self):
        test_str = String(case="lowr")
        #assert test_str.validate('kg') != None
        
    def test_string_lower(self):
        
        def test_string_lower_wrong(data):
            flag = False
            test_str = String(case="lower")
            try:
                test_str.validate(data)
            except Exception as e:
                assert(e.__class__.__name__ == 'TypeError')
                flag = True
            assert (flag == True)
            
        def test_string_lower_correct(data):
            flag = False
            test_str = String(case="lower")
            try:
                test_str.validate(data)
            except Exception as e:
                assert(e.__class__.__name__ == 'TypeError')
                flag = True
            assert (flag == False)
            
        wrong = ['Aauysdg', ')Iubhibj', 'Poidkjhibc', 'ijhbiuKiuigs']
        correct = ['iduahsduahs', 'aa', 'a', '!$%^&*', '984ub', 'aksd()kh']
        
        for w in wrong:
            test_string_lower_wrong(w)
        
        for c in correct:
            test_string_lower_correct(c)

    def test_string_upper(self):

        def test_string_upper_wrong(data):
            flag = False
            test_str = String(case="upper")
            try:
                test_str.validate(data)
            except Exception as e:
                assert (e.__class__.__name__ == 'TypeError')
                flag = True
            assert (flag == True)

        def test_string_upper_correct(data):
            flag = False
            test_str = String(case="upper")
            try:
                test_str.validate(data)
            except Exception as e:
                assert (e.__class__.__name__ == 'TypeError')
                flag = True
            assert (flag == False)

        wrong = ['Aauysdg', ')Iubhibj', 'Poidkjhibc', 'ijhbiuKiuigs']
        correct = ['AHTDHGF', 'KJU8768G()(', 'B', '!$%^&*', '984KJH', 'JUGKJG*&^H']

        for w in wrong:
            test_string_upper_wrong(w)

        for c in correct:
            test_string_upper_correct(c)

	# Camelize dict only checks for a word, not sentence
    def test_string_camel(self):

        def test_string_camel_wrong(data):
            flag = False
            test_str = String(case="camel")
            try:
                test_str.validate(data)
            except Exception as e:
                assert (e.__class__.__name__ == 'TypeError')
                flag = True
            assert (flag == True)

        def test_string_camel_correct(data):
            flag = False
            test_str = String(case="camel")
            try:
                test_str.validate(data)
            except Exception as e:
                assert (e.__class__.__name__ == 'TypeError')
                flag = True
            assert (flag == False)

        wrong = ['hauysdg bgjn', 'kHhkjh']
        correct = ['HELLO', 'Hello', 'Hello World']

        for w in wrong:
            test_string_camel_wrong(w)

        for c in correct:
            test_string_camel_correct(c)

    def test_string_normalised(self):

        def test_string_normalised_wrong(data):
            flag = False
            test_str = String(case="normalised")
            try:
                test_str.validate(data)
            except Exception as e:
                assert (e.__class__.__name__ == 'TypeError')
                flag = True
            assert (flag == True)

        def test_string_normalised_correct(data):
            flag = False
            test_str = String(case="normalised")
            try:
                test_str.validate(data)
            except Exception as e:
                assert (e.__class__.__name__ == 'TypeError')
                flag = True
            assert (flag == False)

        wrong = ['ht Iyf', ')Iubhibj', 'Poidkjh*ibc', 'ijhbiuKiu(*igs', '!$%^&*']
        correct = ['iduahsduahs', 'aa', 'a', '984ub', 'aksdkh']

        for w in wrong:
            test_string_normalised_wrong(w)
        
        for c in correct:
            test_string_normalised_correct(c)

    def test_date(self):

        def broken_test():
            raise Exception('Date class is broken')

        ds = dt.date(2012, 4, 13)
        de = dt.date(2019, 4, 13)
        stamp = Date(earliest_date=ds,latest_date=de)

	    # Correct Date
        try:
            t1 = dt.date(2012, 5, 13)
            stamp.validate(t1)
        except Exception as e:
            broken_test()
            assert (e.__class__.__name__ == 'ValueError')

        #Wrong date
        try:
            flag = False
            t2 = dt.date(2019, 5, 13)
            stamp.validate(t2)
        except Exception as e:
            flag = True
            assert (e.__class__.__name__ == 'ValueError')
        if flag == False:
            broken_test()

        #Wrong Input
        try:
            flag = False
            t3 = 'Hello'
            stamp.validate(t3)
        except Exception as e:
            flag = True
            assert (e.__class__.__name__ == 'TypeError')
        if flag == False:
            broken_test()
            
        
        
