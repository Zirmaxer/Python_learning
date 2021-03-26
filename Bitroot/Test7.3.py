'''
Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *)
з належною перевіркою й обробкою помилок.
'''


class Fraction:
    def __init__(self, x, y):
        if y == 0:
            raise ZeroDivisionError
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        # Сложение.
        if self.y < other.y:
            min_y = self.y
            max_y = other.y
            min_x = self.x
            max_x = other.x
        else:
            min_y = other.y
            max_y = self.y
            min_x = other.x
            max_x = self.x

        if self.y == other.y:  # Ситуация, если знаменатель общий
            xx = self.x + other.x
            yy = self.y
            print(f'Fraction({xx}, {yy})')
            return Fraction(xx, yy)
        elif max_y % min_y == 0:  # Ситуация, если знаменатели делятся друг на друга с целой частью
            coef = max_y / min_y
            xx = int((min_x * coef) + max_x)
            yy = int(max_y)
            print(f'Fraction({xx}, {yy})')
            return Fraction(xx, yy)
        else:  # Ситуация, если знаменатели разные и не делятся в целую
            coef = min_y * max_y
            coef_min = coef / min_y
            coef_max = coef / max_y
            xx = int((min_x * coef_min) + (max_x * coef_max))
            yy = int(coef)
            print(f'Fraction({xx}, {yy})')
            return Fraction(xx, yy)

    def __sub__(self, other):
        # Вычитание.
        if self.y < other.y:
            min_y = self.y
            max_y = other.y
            min_x = self.x
            max_x = other.x
            place = 1
        else:
            min_y = other.y
            max_y = self.y
            min_x = other.x
            max_x = self.x
            place = 2

        if self.y == other.y:  # Ситуация, если знаменатель общий
            xx = self.x - other.x
            yy = self.y
            print(f'Fraction({xx}, {yy})')
            return Fraction(xx, yy)
        elif max_y % min_y == 0:  # Ситуация, если знаменатели делятся друг на друга с целой частью
            coef = max_y / min_y
            if place == 2:
                xx = int((min_x * coef) - max_x)
            else:
                xx = int(max_x - (min_x * coef))
            yy = int(max_y)
            print(f'Fraction({xx}, {yy})')
            return Fraction(xx, yy)
        else:  # Ситуация, если знаменатели разные и не делятся в целую
            coef = min_y * max_y
            coef_min = coef / min_y
            coef_max = coef / max_y
            if place == 2:
                xx = int((min_x * coef_min) - (max_x * coef_max))
            else:
                xx = int((max_x * coef_max) - (min_x * coef_min))
            yy = int(coef)
            print(f'Fraction({xx}, {yy})')
            return Fraction(xx, yy)

    def __mul__(self, other):
        # Умножение.
        xx = int(self.x * other.x)
        yy = int(self.y * other.y)
        print(f'Fraction({xx}, {yy})')
        return Fraction(xx, yy)

    def __truediv__(self, other):
        # Деление, оператор /.
        if other.x == 0 or other.y == 0 or self.y == 0:
            raise ZeroDivisionError
        else:
            xx = int(self.x * other.y)
            yy = int(self.y * other.x)
            if xx % yy == 0:
                coef = xx / yy
                xx = int(xx / coef)
                yy = int(yy / coef)
            return Fraction(xx, yy)

    def __repr__(self):
        return f'Fraction({self.x}, {self.y})'

    def __eq__(self, other):
        if str(self) == str(other):
            return True
        else:
            return False


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
