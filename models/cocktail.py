from models.drink import Drink
from models.enums.cup_type import CupType
from models.enums.country import Country


class Cocktail(Drink):
    def __init__(self, receipt: str, cup_type: CupType,
                 name: str, price: int, volume_in_ml: int, country: Country):
        self.receipt = receipt
        self.cup_type = cup_type
        super().__init__(name, price, volume_in_ml, country)

    def set_receipt(self, receipt):
        self.receipt = receipt

    def get_receipt(self):
        return self.receipt

    def set_cup_type(self, cup_type):
        self.cup_type = cup_type

    def get_cup_type(self):
        return self.cup_type
