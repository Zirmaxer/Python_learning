'''
Напишіть клас TypeDecorators, який має різні методи конвертації результатів функцій у зазначений
тип, якщо це неможливо – викликати відповідний виняток.
Методи:
to_int
to_str
to_bool
to_float
Не забувайте використовувати @wraps
'''

from functools import wraps


class TypeDecorators:
    pass

    def to_int(self):
        def inner(value):
            try:
                return int(value)
            except:
                raise TypeError

        return inner

    def to_str(self):
        def inner(value):
            try:
                return str(value)
            except:
                return None

        return inner

    def to_float(self):
        def inner(value):
            try:
                return float(value)
            except:
                return None

        return inner

    def to_bool(self):
        def inner(value):
            try:
                return value
            except:
                return None

        return inner


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('hello') is True
