from models.enums.sort_order import SortOrder
from models.enums.coffee_type import CoffeeType


class CoffeeMineManager:

    def __init__(self, drinks: []):
        self.drinks = drinks

    def add_drinks(self, drinks: []):
        self.drinks += drinks

    def sort_by_price(self, drinks: [] = None, order: SortOrder = 0):
        return sorted(drinks if drinks else self.drinks, key=lambda i: i.get_price(),
                      reverse=order.value if order else False)

    def sort_by_amount_of_coffee(self, drinks: [] = None, order: SortOrder = 0):
        return sorted(drinks if drinks else self.drinks, key=lambda i: i.get_coffee_weight(),
                      reverse=order.value if order else False)

    def search_by_coffee(self, coffee_type: CoffeeType):
        return f"Finded coffee with type {coffee_type.name}: " \
               f"{[drink for drink in self.drinks if drink.get_coffee_type() == coffee_type]}"
