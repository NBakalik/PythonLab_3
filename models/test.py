from models.coffee import Coffee
from .enums.coffee_type import CoffeeType
from .enums.cup_type import CupType
from .enums.country import Country
from models.cognac import Cognac
from managers.coffee_mine_manager import CoffeeMineManager
from pprint import pprint
from models.recipe import Recipe
from models.enums.ingredient import Ingredient


class Test:
    def main(self):
        espresso = Coffee(CoffeeType.GROUND, 30, "espresso", 100, 250, Country.BRAZIL)
        americano = Coffee(CoffeeType.INSTANT_BAGS, 25, "americano", 80, 250, Country.BRAZIL)
        cappuccino = Coffee(CoffeeType.GRAIN, 40, "cappuccino", 75, 300, Country.FRANCE)

        ararat_apricot = Cognac(5, 2000, 40, "ARARAT Apricot 5*", 300, 50, Country.GERMANY)

        coffee_manager = CoffeeMineManager([espresso, americano, cappuccino, ararat_apricot])
        print("------------ALL DRINKS IN COFFEE MINE:------------")
        pprint(coffee_manager.drinks)
        print("------------SORTED DRINKS BY PRICE IN COFFEE MINE:------------")
        pprint(coffee_manager.sort_by_price())
        print("------------SORTED DRINKS BY AMOUNT OF COFFEE IN COFFEE MINE:------------")
        pprint(coffee_manager.sort_by_amount_of_coffee([espresso, americano, cappuccino]))
        print("------------SEARCHED COFFEE BY COFFEE_TYPE IN COFFEE MINE:------------")
        coffee_manager.drinks.pop()
        print(coffee_manager.search_by_coffee(CoffeeType.GRAIN))

        recipe_of_mojito = Recipe("description", [Ingredient.MINT, Ingredient.LEMON, Ingredient.VODKA],
                                  "Make something and done", CupType.MARGARITA, "mojito", 150, 300, Country.ITALY)

        print("------------RECIPE:------------")
        print(recipe_of_mojito.cocktail)
