import unittest
from into_py import into


class TestIntoPy(unittest.TestCase):

    def test_into_assigns_result_of_expression_to_variable(self):
        def add(x, y):
            return x + y

        result = into(sum, [1, 2, 3], add)

        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
