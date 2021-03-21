from models.drink import Drink
from models.enums.country import Country


class AlcoholDrink(Drink):
    def __init__(self, year: int, alcohol_by_volume: int,
                 name: str, price: int, volume_in_ml: int, country: Country):
        self.year = year
        self.alcohol_by_volume = alcohol_by_volume
        super().__init__(name, price, volume_in_ml, country)

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_alcohol_by_volume(self, alcohol_by_volume):
        self.alcohol_by_volume = alcohol_by_volume

    def get_alcohol_by_volume(self):
        return self.alcohol_by_volume