from Fibonachi import fibonacci
import unittest

class TestFibonacci(unittest.TestCase):
    """Fibonacci tests"""
    def test_fibonacci(self):
        nat1 = fibonacci(21)
        nat2 = fibonacci(4)
        self.assertTrue(nat1, True)
        self.assertFalse(nat2, False)

if __name__ == '__main__':
    unittest.main()