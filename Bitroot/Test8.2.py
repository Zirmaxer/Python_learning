'''
Напишіть Python-функцію під назвою operation_mapper, яка приймає на вхід математичну операцію у
вигляді рядка: “+”, “-”, “/”, “*”, “**” (в іншому випадку, має викликатися правильний виняток
ValueError); має повертатися функція, яка працює з двома вхідними параметрами, застосовує
математичну операцію до них і повертає результат.
'''


def _add(x, y):
    return x+y


def _div(x, y):
    if y == 0:
        raise ValueError ('y cant be a zero')
    else:
        return x/y


def _sub(x, y):
    return x-y


def _mul(x, y):
    return x*y


def _default(*args, **kwargs):
    raise ValueError


def operation_mapper(operation):
    command_dict = {
        '+': _add,
        '-': _sub,
        '/': _div,
        '*': _mul
    }
    if operation in command_dict:
        return command_dict[operation]
    else:
        return _default
