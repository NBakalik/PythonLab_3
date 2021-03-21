from models.alcohol_drink import *
from models.enums.wine_type import WineType


class Wine(AlcoholDrink):
    def __init__(self, wine_type: WineType, year: int, alcohol_by_volume: int,
                 name: str, price: int, volume_in_ml: int, country: Country):
        self.wine_type = wine_type
        super().__init__(year, alcohol_by_volume, name, price, volume_in_ml, country)

    def set_wine_type(self, wine_type):
        self.wine_type = wine_type

    def get_wine_type(self):
        return self.wine_type
