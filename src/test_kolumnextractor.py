import unittest

import kolumnextractor as kea

test_file = "data/test.csv"


class TestMain(unittest.TestCase):
    def test01(self):
        "Check if it can extract column 1"
        test_column = "column 1"
        class Name(kea.Data):
            _columns = {
                "column1": kea.Number(minvalue=1, maxvalue=100)
            }
        expected_result = [['column 1'], ['1']]
        test = kea.reading_data(filepath=test_file, columns=Name)


if __name__ == '__main__':
    unittest.main()
