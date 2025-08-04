
# AI-suggested unit test:
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 0), "Error: Division by zero")

if __name__ == '__main__':
    unittest.main()
