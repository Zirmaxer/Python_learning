'''
Створіть власну реалізацію ітерованого об'єкта MyIterable, який можна використати всередині циклу
for-in. Також додайте логіку отримання елементів за допомогою квадратних дужок.
'''


class MyIterable:
    def __init__(self, *args):
        self.data = list(args)
        self.index = -1

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.data):
            raise StopIteration
        return self.data[self.index]

    def __getitem__(self, number):
        if not isinstance(number, int):
            raise TypeError('must be integer index')
        if number < 0 or number > len(self.data):
            raise ValueError('index out of range')
        return self.data[number]

    def __setitem__(self, number, value):
        if not isinstance(number, int):
            raise TypeError('must be integer index')
        if number < 0 or number > len(self.data):
            raise ValueError('index out of range')
        self.data[number] = value