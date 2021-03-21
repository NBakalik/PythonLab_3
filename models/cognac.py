from models.alcohol_drink import *


class Cognac(AlcoholDrink):
    def __init__(self, stars: int, year: int, alcohol_by_volume: int,
                 name: str, price: int, volume_in_ml: int, country: Country):
        self.stars = stars
        super().__init__(year, alcohol_by_volume, name, price, volume_in_ml, country)

    def set_stars(self, stars):
        self.stars = stars

    def get_stars(self):
        return self.stars
