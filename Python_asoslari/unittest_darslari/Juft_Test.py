from juft import Juft
import unittest

class JuftTest(unittest.TestCase):
    """Juft sonlar funksiyasi uchun test"""
    def test_juft(self):
        sonlar = [6,5,2,9,7,8,1,3,4,9,1,5,54,6,54,65,95,9]
        juft = Juft(sonlar)
        self.assertEqual(juft, [6,2,8,4,54,6,54])

if __name__ == '__main__':
    unittest.main()