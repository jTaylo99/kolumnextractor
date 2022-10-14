import unittest

from main import reading

class TestMain(unittest.TestCase):
	def test01(self):
		"Check if it can extract column 1"
		test_file = "test.csv"
		test_column = "column 1"
		expected_result = [['column 1'], ['1']]
		test = reading(filepath=test_file, columns=[test_column])
		self.assertEqual(test, expected_result)

if __name__ == '__main__':
	unittest.main()