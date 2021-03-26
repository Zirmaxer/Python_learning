'''
Напишіть клас Ball(color:str) з інформативними методами __repr__ та __str__.
'''


class Ball:
    def __init__(self, color):
        self.color = str(color)

    def __repr__(self):
        return f'This is REPR and color is {self.color}'

    def __str__(self):
        return f'This is STR and color is {self.color}'


