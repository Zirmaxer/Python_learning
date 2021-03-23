'''
Реалізуйте клас Mathematician, який буде допоміжним класом для проведення математичних операцій над списком цілих чисел. Клас не приймає жодних атрибутів і має тільки методи:
(1) square_nums (приймає список цілих чисел і повертає список їхніх квадратів);
(2) remove_positives (приймає список цілих чисел і повертає його без додатних чисел);
(3) filter_leaps (приймає список років (цілих чисел) і прибирає невисокосні).
Ці методи мають бути не визначені безпосередньо в цьому класі, а отримані за допомогою
наслідування з трьох базових класів із цими методами. Іншими словами, потрібно створити три окремі
класи, які інкапсулюють описану логіку, але клас Mathematician потримує її через наслідування.
Також потрібно створити окремий клас, який валідує параметр, переданий у методи.
Має викликатися TypeError, якщо параметр не є списком, і ValueError, якщо переданий список не
є списком цілих чисел.
'''

class ValidationMixin:

    def validate(self, list_int):
        if type(list_int) != list:
            raise TypeError
        else:
            try:
                for item in list_int:
                    tmp = float (item)
            except ValueError as er:
                raise ValueError


class SquareNums(ValidationMixin):

    def square_nums(self, list_int):
        self.validate(list_int)
        return [l*l for l in list_int]


class RemovePositives(ValidationMixin):

    def remove_positives(self, list_int):
        self.validate(list_int)
        return [l for l in list_int if l < 0]


class FilterLeaps:

    def filter_leaps(self, list_int):
        self.validate(list_int)
        return [l for l in list_int if l % 4 == False and l > 0]


class Mathematician(FilterLeaps, RemovePositives, SquareNums):
    ...


if __name__ == "__main__":
    m = Mathematician()

    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]


