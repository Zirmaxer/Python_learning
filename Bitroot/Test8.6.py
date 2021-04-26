'''
Напишіть параметризований декоратор (додаткови рівень декората, що може приймати параметри)
string_arg_rules, який перевіряє позиційні аргументи, що передаються будь-якій задекорованій
функції. При цьому цей декоратор гарантує, що всі позиційні аргументи є рядками та відповідають
визначеним у декораторі вимогам.
Декоратор має приймати 3 аргументи:
- max_length - целое число, допустимая длина входной строки
- contains - кортеж символов, который должен содержать аргумент, по умолчанию пустой кортеж
- exclude - кортеж символов, который не должен содержать аргумент, по умолчанию пустой кортеж

В случае провала любой из проверок, ваш декоратор должен вызвать соответствующее исключение с
сообщением об ошибке, перед любым выполнением декорированной функции. У разі провалу будь-якої
з перевірок, ваш декоратор має викликати відповідний виняток (TypeError або ValueError) з
повідомленням про помилку, перед будь-яким виконанням функції, що декорується.
Для перевірки спробуйте використати декоратор на різних функціях, які приймають різні набори
аргументів.

'''
from functools import wraps


def string_arg_rules(max_length=1, contains=(), exclude=()):
    def call_function(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Блок проверки длины аргументов фцнкции
            if len(args[0]) > max_length:
                raise ValueError(f"Arguments ca'nt be longer than max_length={max_length}")
            # Блок проверки содержит ли аргумент символы из contains
            index = 0
            for item_contains in contains:
                if item_contains in args[0]:
                    index += 1
            if index == 0:
                raise ValueError(f"Arguments must contain {contains}")
            # Блок проверки не содержит ли аргументы символы из exclude
            index = 0
            for item_exclude in exclude:
                if item_exclude in args[0]:
                    index += 1
            if index > 0:
                raise ValueError(f"Arguments can't have contain {exclude}")
            print(f.__name__)
            print(args[0])
            return f(*args, **kwargs)

        return wrapper

    return call_function


@string_arg_rules(max_length=15, contains=['05', '@'], exclude=("S", 's'))
def create_slogan(name: str) -> str:
    return (f"{name} drinks pepsi in his brand new BMW!")


if __name__ == "__main__":
    create_slogan('peter05')  # ok
    create_slogan('peter06')  # ValueError: Arguments must contain '@'
