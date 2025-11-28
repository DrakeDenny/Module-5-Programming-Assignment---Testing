
import unittest


def add_numbers(a, b):
    """Adds two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Multiplies two numbers."""
    return a * b

def divide_numbers(a, b):
    """Divides a by b. Returns None if division by zero."""
    if b == 0:
        return None
    return a / b



class TestMathFunctions(unittest.TestCase):
    
    # Tests for add_numbers
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
    
    # Tests for multiply_numbers
    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(4, 5), 20)
        self.assertEqual(multiply_numbers(-1, 5), -5)
        self.assertEqual(multiply_numbers(0, 100), 0)
    
    # Tests for divide_numbers
    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertIsNone(divide_numbers(10, 0))
        self.assertEqual(divide_numbers(-10, 2), -5)


if __name__ == '__main__':
    unittest.main()
