class Beverage():
    def __init__ (self, ingredients):
        self.ingredients = ingredients
    def get_cost(self):
        mystr = ''
        cost = 0
        for item in self.ingredients:
            for key, value in prices.items():
                if item == key:
                    cost = cost + value
                    mystr = ('%.2f' % cost)
        return f'${mystr}'
    def get_price (self):
        price = 0
        for item in self.ingredients:
            for key, value in prices.items():
                if item == key:
                    price = price + value*2.5
                    mystr = ('%.2f' % price)
        return f'${mystr}'
    def get_name (self):
        output = ''
        if len(self.ingredients)==1:
            output = self.ingredients[0] + ' Smoothie'
            output = output.replace ('Raspberries','Raspberry')
            output = output.replace ('Blueberries','Blueberry')
            output = output.replace ('Strawberries','Strawberry')
            return output
        else:
            self.ingredients.sort()
            for item in self.ingredients:
                output = output + item + ' '
            output += 'Fusion'
            output = output.replace ('Raspberries','Raspberry')
            output = output.replace ('Blueberries','Blueberry')
            output = output.replace ('Strawberries','Strawberry')
            return output