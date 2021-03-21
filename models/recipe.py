from models.cocktail import Cocktail
from models.enums.ingredient import Ingredient
from models.enums.cup_type import CupType
from models.enums.country import Country


class Recipe:
    def __init__(self, description: str, ingredients: list[Ingredient], receipt: str, cup_type: CupType,
                 name: str, price: int, volume_in_ml: int, country: Country):
        self.description = description
        self.ingredients = ingredients
        self.cocktail = Cocktail(receipt, cup_type, name, price, volume_in_ml, country)

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients

    def get_ingredients(self):
        return self.ingredients
