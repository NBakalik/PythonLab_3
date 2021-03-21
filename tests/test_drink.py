from models.drink import Drink
from models.enums.country import Country
import unittest


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.water = Drink("water", 120, 250, Country.ITALY)

    def test_init(self):
        self.assertEqual(self.water.name, "water")
        self.assertEqual(self.water.price, 120)
        self.assertEqual(self.water.volume_in_ml, 250)
        self.assertEqual(self.water.country, Country.ITALY)

    def test_repr(self):
        self.assertEqual(self.water.__repr__(), "name: water, price: 120, volume in ml: 250, country: Country.ITALY")
