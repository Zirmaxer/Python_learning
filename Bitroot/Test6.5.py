'''
Створіть власний виняток під назвою CustomException. Можна успадкувати від базового класу Exception,
але розширте його функціональність так, щоб він приймав спеціальний іменний аргумент file_log_msg,
який повинен логуватися до файлу logs.txt. Якщо жоден параметр file_log_msg не переданий,
використовуйте перший позиційний аргумент як стандартне значення. В іншому випадку пропустіть
логування до файлу.
'''


class CustomException(Exception):
    _file = "logs.txt"

    def __init__(self, *args, file_log_msg='', **kwargs):
        if file_log_msg == '' and args == () and kwargs == {}:
            pass
        elif file_log_msg == '' and args != ():
            with open("logs.txt", 'a') as my_file:
                tmp = args[0]
                my_file.write(str(tmp))
                my_file.write('\n')
        elif file_log_msg == '' and kwargs != {}:
            with open("logs.txt", 'a') as my_file:
                for i,k in kwargs.items():
                    tmp = k
                    my_file.write(str(tmp))
                    my_file.write('\n')
                    break
        else:
            with open("logs.txt", 'a') as my_file:
                my_file.write(file_log_msg)
                my_file.write('\n')


if __name__ == "__main__":
    raise CustomException(file_log_msg='', aa='sdfdsdf', bb='222')
