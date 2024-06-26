import unittest
from main import Ful_name

class TestFulName(unittest.TestCase):
    def test_full_name(self):
        name = Ful_name("john", "dOe")
        self.assertEqual(name, "John Doe")

if __name__ == '__main__':
    unittest.main()
