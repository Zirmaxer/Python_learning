'''
Створіть функцію sum_of_digits, яка приймає введення рядків і повертає суму всіх символів
переданого рядка (тобто числового представлення символу). Функція працює тільки з рядками,
і якщо переданий об'єкт іншого типу, вона повинна викликати TypeError. Вам потрібно реалізувати
цю функцію виключно за допомогою рекурсії.
def sum_of_digits(digit_string):
    """
    >>> sum_of_digits('2g6t') == 8
    True

    >>> sum_of_digits(True)
    TypeError("input string must be string")
    """
'''


def sum_of_digits(digit_string):
    tmp = 0
    if not isinstance(digit_string, str):
        raise TypeError("input string must be string")
    if len(digit_string) > 0 and digit_string[-1].isdigit():
        tmp = int(digit_string[-1])
    if digit_string == '':
        return 0
    return tmp + sum_of_digits(digit_string[0:-1])