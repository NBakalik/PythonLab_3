from models.recipe import Recipe
from models.enums.country import Country
from models.enums.ingredient import Ingredient
from models.enums.cup_type import CupType
import unittest


class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.recipe_of_mojito = Recipe("description", [Ingredient.MINT, Ingredient.LEMON, Ingredient.VODKA],
                                       "Make something and done", CupType.MARGARITA, "mojito", 150, 300, Country.ITALY)

    def test_init(self):
        self.assertEqual(self.recipe_of_mojito.cocktail.__repr__(),
                         "name: mojito, price: 150, volume in ml: 300, country: Country.ITALY")
        self.assertEqual(self.recipe_of_mojito.description, "description")
        self.assertEqual(self.recipe_of_mojito.get_ingredients(), [Ingredient.MINT, Ingredient.LEMON, Ingredient.VODKA])
