'''
Створіть функцію to_power, яка приймає два параметри: x та exp, і повертає x ^ exp.
Вам потрібно реалізувати цю функцію виключно за допомогою рекурсії. Приклад:
Returns x ^ exp
>>> to_power(2, 3) == 8
True
>>> to_power(3.5, 2) == 12.25
True
>>> to_power(2, -1)
ValueError: This function works only with exp > 0.
'''

def to_power(x, exp):
    if exp < 0:
        raise ValueError('This function works only with exp > 0.')
    if exp == 1:
        return x
    return x * to_power(x, exp-1)
