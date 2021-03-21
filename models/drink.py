from models.enums.country import Country


class Drink:
    def __init__(self, name: str, price: int, volume_in_ml: int, country: Country):
        self.name = name
        self.price = price
        self.volume_in_ml = volume_in_ml
        self.country = country

    def __repr__(self):
        return f"name: {self.name}, price: {self.price}, volume in ml: {self.volume_in_ml}, country: {self.country}"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_volume(self, volume_in_ml):
        self.volume_in_ml = volume_in_ml

    def get_volume(self):
        return self.volume_in_ml

    def set_country(self, country: Country):
        self.country = country

    def get_country(self):
        return self.country
