'''
Реалізація функції open, частина 2

Це завдання розширює попереднє, але цього разу потрібно створити комплексний wrapper для всієї
функціональності вбудованої функції open. Потрібно створити користувацький клас
CounterLoggingFileOpen, але цього разу екземпляри класу повинні мати можливість викликатись
напряму з такими ж атрибутами, як і вбудована функція open (в навчальних цілях, зупинимося на
атрибутах file і mode) і повертати об'єкт File, тобто результат виклику вбудованої open з тими ж
атрибутами. Ми додамо гнучкості нашим екземплярам класу CounterLoggingFileOpen, розмістивши
атрибути logger_file і counter в кожному екземплярі замість атрибутів класу. Перегляньте приклади
використання у блоці if __name__ == “__main__” .
Стосовно логіки лічильника та логування в попередній версії, їх також потрібно замінити, щоб вони
були сумісні з новою функціональністю класу. Нам потрібно логувати повідомлення в форматі:
{counter} -- {current_date} -- {file} -- {mode} -- {size of the file in bytes}
до лог-файлу, розміщеного в атрибуті logger_file екземпляра класу. Зверніть увагу, що логування
відбувається на кожне успішне відкриття файлу. Якщо відкриття не вдалося з якихось причин,
логування не має відбуватися.
'''

import os
import datetime
import re


class CounterLoggingFileOpen:

    def __init__(self, logger_file='test_logs.txt', counter=0):
        self._file = None
        self._file_type = None
        self.logger_file = logger_file
        self.counter = counter

    def __call__(self, file_name, file_type='r'):
        if not isinstance(file_name, str) or not isinstance(file_type, str):
            raise TypeError ('not str')
        if not re.fullmatch('[rwxa][bt+]?', file_type):
            raise ValueError('error mode of reading file')
        self._file = file_name
        self._file_type = file_type
        self.log = open(self.logger_file, 'a')
        self.f = open(self._file, self._file_type)
        self.counter += 1

        my_date =  datetime.date.today()
        if not os.path.isfile(file_name):
            file_size = 0
        else:
            file_size = os.path.getsize(file_name)
        log_message = f"{self.counter} -- {my_date} -- {self._file} -- {self._file_type} -- {file_size}\n"
        self.log.write(log_message)
        return self

    def __enter__(self):
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        self.log.close()
        return True

    def write(self, message):
        with open(self._file, self._file_type) as myfile:
            myfile.write(message)

    def read(self):
        return self.f.read()

    def close(self):
        self.log.close()
        return self.f.close()

if __name__ == "__main__":
    f1 = CounterLoggingFileOpen('test_log.txt')

    with f1('test.txt', 'w') as f:
        f.write('hello')

    with f1('test.txt', 'r') as f:
        s = f.read()

    #print(s)
    # Prints to stdout
    # "hello"

    f = f1('test_log.txt')
    s = f.read()
    f.close()
    print(s)
    # Prints to stdout
    # 1 -- 2020-11-06 -- test.txt -- w -- 0
    # 2 -- 2020-11-06 -- test.txt -- r -- 5
    # 3 -- 2020-11-06 -- test_log.txt -- r -- 76
