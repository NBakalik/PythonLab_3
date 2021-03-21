from models.coffee import Coffee
from models.cognac import Cognac
from models.drink import Drink
from models.recipe import Recipe
from models.enums.coffee_type import CoffeeType
from models.enums.country import Country
from models.enums.sort_order import SortOrder
from models.enums.ingredient import Ingredient
from models.enums.cup_type import CupType
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


class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.recipe_of_mojito = Recipe("description", [Ingredient.MINT, Ingredient.LEMON, Ingredient.VODKA],
                                       "Make something and done", CupType.MARGARITA, "mojito", 150, 300, Country.ITALY)

    def test_init(self):
        self.assertEqual(self.recipe_of_mojito.cocktail.__repr__(),
                         "name: mojito, price: 150, volume in ml: 300, country: Country.ITALY")
        self.assertEqual(self.recipe_of_mojito.description, "description")
        self.assertEqual(self.recipe_of_mojito.get_ingredients(), [Ingredient.MINT, Ingredient.LEMON, Ingredient.VODKA])


if __name__ == '__main__':
    unittest.main()
