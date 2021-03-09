from models.drink import Drink
from models.enums.coffee_type import CoffeeType
from models.enums.country import Country


class Coffee(Drink):
    def __init__(self, coffee_type: CoffeeType, coffee_weight: int,
                 name: str, price: int, volume_in_ml: int, country: Country):
        self.coffee_type = coffee_type
        self.coffee_weight = coffee_weight
        super().__init__(name, price, volume_in_ml, country)

    def set_coffee_type(self, coffee_type):
        self.coffee_type = coffee_type

    def get_coffee_type(self):
        return self.coffee_type

    def set_coffee_weight(self, coffee_weight):
        self.coffee_weight = coffee_weight

    def get_coffee_weight(self):
        return self.coffee_weight
