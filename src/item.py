class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description


class Condiment(Item):
    def __init__(self, item_name, item_description, bonus_points):
        self.bonus_points = bonus_points
        super().__init__(item_name, item_description)

    def __str__(self):
        return f"{self.item_name}, {self.item_name}"


class Drink(Item):
    def __init__(self, item_name, item_description, bonus_points):
        self.bonus_points = bonus_points
        super().__init__(item_name, item_description)

    def __str__(self):
        return f"{self.item_name}, {self.item_name}"


class Dessert(Item):
    def __init__(self, item_name, item_description, bonus_points):
        self.bonus_points = bonus_points
        super().__init__(item_name, item_description)

    def __str__(self):
        return f"{self.item_name}, {self.item_name}"
