import unittest
from calculator import add, subtract, multiply, divide


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 4), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)


if __name__ == '__main__':
    unittest.main()
