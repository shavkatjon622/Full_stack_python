from royxat import Katta
import unittest

class RoxatTest(unittest.TestCase):
    """Matnlar katta harfligini tekshiruvchi test class"""
    def test_katta(self):
        result = Katta('assalomu alaykum', 'assalomu alaykum')
        self.assertEqual(result, 'Assalomu Alaykum', 'Assalomu Alaykum')

if __name__ == '__main__':
    unittest.main()