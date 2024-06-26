import unittest
from user_classi import Shaxs, Talaba

class TestShaxs(unittest.TestCase):

    def setUp(self):
        name = "shavkatjon"
        surname = "vahobov"
        passport = "AC2684586"
        tyil = 2004
        self.shaxs1 = Shaxs(name, surname, passport, tyil)

    def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
    def test_get_info(self):
        self.assertEqual(self.shaxs1.get_info(), "Shavkatjon Vahobov. Passport:AC2684586, 2004-yilda tug`ilgan")
    def test_age(self):
        natija = self.shaxs1.get_age(2024)
        self.assertEqual(natija, 20)


class TestTalaba(unittest.TestCase):

    def setUp(self):
        name = "shavkatjon"
        surname = "vahobov"
        passport = "AC2684586"
        tyil = 2004
        self.talaba1 = Talaba(name, surname, passport, tyil, 594152198)

    def test_create(self):
        self.assertTrue(isinstance(self.talaba1, Shaxs))
        self.assertIsNotNone(self.talaba1.ism)
        self.assertIsNotNone(self.talaba1.familiya)
        self.assertIsNotNone(self.talaba1.passport)
        self.assertIsNotNone(self.talaba1.tyil)
        self.assertIsNotNone(self.talaba1.idraqam)

    def test_get_id(self):
        self.assertEqual(self.talaba1.get_id(), 594152198)

    def test_get_bosqich(self):
        self.assertEqual(self.talaba1.get_bosqich(), 1)

    def test_get_info(self):
        self.assertEqual(self.talaba1.get_info(), "Shavkatjon Vahobov. 1-bosqich. ID raqami: 594152198")

    def test_age(self):
        natija = self.talaba1.get_age(2024)
        self.assertEqual(natija, 20)


if __name__ == '__main__':
    unittest.main()