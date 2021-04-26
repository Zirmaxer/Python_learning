'''
Створіть власний клас CounterLoggingFileOpen, який реалізує протокол контекстного менеджера в
Python і поводиться як вбудована функція open, але тільки як контекстний менеджер. Подивіться на
приклад в блоці if __name__ == “__main__” .
Також потрібно розширити його функціонал лічильником і логуванням, щоб наша реалізація класу могла
б використовуватись як допоміжна обгортка для вбудованої функції open.
Щоразу, коли цей контекстний менеджер використовується у виразі with або при прямому виклику
методу __enter__, його лічильник повинен інкрементуватися з показом повідомлення в форматі:
“{index}. File: {file path} Mode: {used mode to open the file} Error: {any error raised during
activated context}”
Приклад:
1. File: 'test.txt' Mode: 'w' Error: None
Зверніть особливу увагу на реалізацію методу __exit__, який має замовчувати будь-яку помилку під
час виконання контекстного блоку, але логувати тип помилки до лог-файлу.
'''


class CounterLoggingFileOpen:
    counter = 0
    logger_file = 'logs.txt'

    # students write your program here
    def __init__(self, file_name, file_type):
        self.file_name = file_name
        self.file_type = file_type

    def __enter__(self):
        CounterLoggingFileOpen.counter += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('logs.txt', 'a') as log_file:
            log_message = f"{CounterLoggingFileOpen.counter}. File: '{self.file_name}' Mode: '{self.file_type}' Error: {exc_type}\n"
            log_file.write(log_message)
        return True

    def write(self, message):
        with open(self.file_name, self.file_type) as myfile:
            myfile.write(message)

    def read(self):
        with open(self.file_name, self.file_type) as myfile:
            output = myfile.read()
            return output


if __name__ == "__main__":
    with CounterLoggingFileOpen('test.txt', 'w') as f:
        f.write('hello')

    with CounterLoggingFileOpen('test.txt', 'r') as f:
        s = f.read()

    with CounterLoggingFileOpen('test.txt', 'r') as f:
        raise TypeError('')

    print(s)  # "hello"
    print("Num of times used", CounterLoggingFileOpen.counter)  # Num of times used 3