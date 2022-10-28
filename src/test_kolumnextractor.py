import unittest

from kolumnextractor import reading

class TestMain(unittest.TestCase):
	def test01(self):
		"Check if it can extract column 1"
		test_file = "../data/test.csv"
		test_column = "column 1"
		expected_result = [['column 1'], ['1']]
		test = reading(filepath=test_file, columns=[test_column])
		self.assertEqual(test, expected_result)

	def test02(self):
		"Check if it can extract column 1 and column 2"
		test_file = "../data/test.csv"
		test_column = ["column 1", "column 2"]
		expected_result = [['column 1', 'column 2'], ['1', '2']]
		test = reading(filepath=test_file, columns=test_column)
		self.assertEqual(test, expected_result)

	def test03(self):
		"Check if it can extract column 1, column 2, and column 3"
		test_file = "../data/test.csv"
		test_column = ["column 1", "column 2", "column 3"]
		expected_result = [['column 1', 'column 2', 'column 3'], ['1', '2', '3']]
		test = reading(filepath=test_file, columns=test_column)
		self.assertEqual(test, expected_result)

	def test04(self):
		"Check if it can extract column 2, and column 3"
		test_file = "../data/test.csv"
		test_column = ["column 2", "column 3"]
		expected_result = [['column 2', 'column 3'], ['2', '3']]
		test = reading(filepath=test_file, columns=test_column)
		self.assertEqual(test, expected_result)

if __name__ == '__main__':
	unittest.main()
