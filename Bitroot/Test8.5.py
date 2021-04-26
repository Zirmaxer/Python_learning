'''
Напишіть декоратор, який робить print функції з переданими їй аргументами.
ПРИМІТКА! Це має бути print імені функції з параметрами, а не результату її виконання!
'''

from functools import wraps

def logger(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if args == ():
            index_args = 0
        else:
            tmp = ''
            for item in args:
                if type(item) == str:
                    tmp += f"'{item}'"
                else:
                    tmp += str(item)
            # index_args =', '.join([str(i) for i in args])
        index_kwargs = ''
        if kwargs != {}:
            for k,v in kwargs.items():
                if type(v) == str:
                    index_kwargs += f'{k}=\'{v}\','
                else:
                    index_kwargs += f'{k}={v},'
        else:
            index_kwargs = {}
        if index_kwargs != {}:
            index_kwargs = index_kwargs[:-1]
            # index_kwargs = ','.join([f'{k}=\'{v}\'' for k,v in kwargs.items()])

        print(f'{f.__name__} called with args: {tmp} and kwargs: {index_kwargs}')
    return wrap

@logger
def test_some1(a):
    return a


@logger
def test_some2(a, b, c):
    return a


print(test_some1(1))  # test_some1 called with args: 1 and kwargs: {}
print(test_some2(2, b='y', c=123))  # test_some2 called with args: 2 and kwargs: b='y',c='e'


