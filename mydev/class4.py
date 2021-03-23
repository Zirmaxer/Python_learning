class Pizza():
    order = 0
    def __init__(self, ingredients):
        Pizza.order += 1
        self.order_number = Pizza.order
        self.ingredients = ingredients
    @classmethod
    def hawaiian (cls):
        return cls(['ham', 'pineapple'])
    @classmethod
    def meat_festival (cls):
        return cls(['beef', 'meatball', 'bacon'])
    @classmethod
    def garden_feast (cls):
        return cls(['spinach', 'olives', 'mushroom'])