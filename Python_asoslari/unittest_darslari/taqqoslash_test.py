from sonlarni_taqqoslash import Taqqoslash
import unittest

class TestTaqqoslash(unittest.TestCase):
    def test_taqqoslash(self):
        taqqoslash = Taqqoslash(5,13,9)
        self.assertEqual(taqqoslash, 13)


if __name__ == '__main__':
    unittest.main()