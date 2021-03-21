from models.coffee import Coffee
from models.cognac import Cognac
from models.enums.coffee_type import CoffeeType
from models.enums.country import Country
from models.enums.sort_order import SortOrder
from managers.coffee_mine_manager import CoffeeMineManager
import unittest


class TestCoffeeMineManager(unittest.TestCase):
    def setUp(self):
        self.espresso = Coffee(CoffeeType.GROUND, 30, "espresso", 100, 250, Country.BRAZIL)
        self.americano = Coffee(CoffeeType.INSTANT_BAGS, 25, "americano", 80, 250, Country.BRAZIL)
        self.cappuccino = Coffee(CoffeeType.GRAIN, 40, "cappuccino", 75, 300, Country.FRANCE)
        self.ararat_apricot = Cognac(5, 2000, 40, "ARARAT Apricot 5*", 300, 50, Country.GERMANY)

        self.coffee_manager = CoffeeMineManager([self.espresso, self.americano, self.cappuccino])

    def test_sort_by_price(self):
        # test sorting default list of drinks without arguments
        self.assertListEqual(self.coffee_manager.sort_by_price(), [self.cappuccino, self.americano, self.espresso])
        # test sorting default list of drinks with DESC order
        self.assertListEqual(self.coffee_manager.sort_by_price(order=SortOrder.DESC),
                             [self.espresso, self.americano, self.cappuccino])
        # test sorting non-default list with ASC order
        self.assertListEqual(self.coffee_manager.sort_by_price([self.americano, self.espresso, self.ararat_apricot],
                                                               order=SortOrder.ASC),
                             [self.americano, self.espresso, self.ararat_apricot])

    def test_add_drinks(self):
        # test add func with list argument
        self.coffee_manager.add_drinks([self.cappuccino, self.ararat_apricot])
        self.assertEqual(self.coffee_manager.drinks,
                         [self.espresso, self.americano, self.cappuccino, self.cappuccino, self.ararat_apricot])
        # test add func without arguments
        self.coffee_manager.add_drinks()
        self.assertEqual(self.coffee_manager.drinks,
                         [self.espresso, self.americano, self.cappuccino, self.cappuccino, self.ararat_apricot])

    def test_sort_by_amount_of_coffee(self):
        # test sorting without arguments(ASC)
        self.assertListEqual(self.coffee_manager.sort_by_amount_of_coffee(),
                             [self.americano, self.espresso, self.cappuccino])

        # test sorting with DESC argument
        self.assertListEqual(self.coffee_manager.sort_by_amount_of_coffee(order=SortOrder.DESC),
                             [self.cappuccino, self.espresso, self.americano])

        # test sorting list with ASC argument
        self.assertListEqual(
            self.coffee_manager.sort_by_amount_of_coffee([self.cappuccino, self.espresso], order=SortOrder.ASC),
            [self.espresso, self.cappuccino])

    def test_search_by_coffee(self):
        # searching by GRAIN type
        self.assertEqual(self.coffee_manager.search_by_coffee(CoffeeType.GRAIN),
                         f'Found coffee with type GRAIN:{[self.cappuccino]}')

        # searching without arguments
        self.assertEqual(self.coffee_manager.search_by_coffee(), [self.espresso, self.americano, self.cappuccino])
