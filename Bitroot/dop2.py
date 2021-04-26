import copy
my_base = []
number = 0


def waiting_answer():
    while True:
        answer = input('Please enter your joice (create, show, sort, quit) :')
        answer = answer.lower()
        if answer == 'create':
            create()
        elif answer == 'show':
            show()
        elif answer == 'sort':
            sort()
        elif answer == 'quit':
            break
        else:
            print('You are entered wrong command. Please enter valid command (create, show, sort, quit):')
            continue


def create():
    # Запрашиваем имя
    while True:
        name = input('Your name: ')
        if check_str(name) is False:
            print('Please reenter your Name (must be only string): ')
            continue
        else:
            break

    # Запрашиваем фамилию
    while True:
        surname = input('Your surname: ')
        if check_str(surname) is False:
            print('Please reenter your Surname (must be only string): ')
            continue
        else:
            break

    # Запрошиваем возраст
    while True:
        age = input('Please enter your age: ')
        if check_int(age) is False or int(age) < 0 or int(age) > 150:
            print('Please reenter your age (must be integer (min 1, max 150): ')
            continue
        else:
            age = int(age)
            break

    # Запрашиваем стаж
    while True:
        experience = input('Please enter your experience: ')
        if check_int(experience) is False or int(experience) > age:
            print('Please reenter your experience (must be integer (less than age): ')
            continue
        else:
            experience = int(experience)
            break

    # Запращиваем уровень зарплаты
    while True:
        salary = input('Please enter your level of salary: ')
        if check_int(salary) is False or int(salary) < 0:
            print('Please reenter your level of salary (must be integer (more than zero): ')
            continue
        else:
            salary = int(salary)
            break

    # Записываем данные в my_base
    global number
    number += 1
    my_base.append({'number': number, 'Name': name.capitalize(), 'Surname': surname.capitalize(), 'Age': age, 'Experience': experience,
                    'Salary': salary})


def show():
    # Узнаем самое длинное значение для каждого столбца таблицы
    name_len = 4
    surname_len = 7
    age_len = 3
    experience_len = 10
    salary_len = 6
    for minidict in my_base:
        for item, value in minidict.items():
            if item == 'Name':
                if len(value) > name_len:
                    name_len = len(value)
            if item == 'Surname':
                if len(value) > surname_len:
                    surname_len = len(value)
            if item == 'Age':
                if len(str(value)) > age_len:
                    age_len = int(len(str(value)))
            if item == 'Experience':
                if len(str(value)) > experience_len:
                    experience_len = int(len(str(value)))
            if item == 'Salary':
                if len(str(value)) > salary_len:
                    salary_len = int(len(str(value)))

    # Функция печати строки
    def my_print(my_dict):
        my_str = ''
        for item, value in my_dict.items():
            if item != 'number':
                my_str += '# '
                my_str += str(value) + ' '
                if item == 'Name' and len(value) < name_len:
                    k = 0
                    for k in range(name_len - len(value)):
                        my_str += ' '
                if item == 'Surname' and len(value) < surname_len:
                    k = 0
                    for k in range(surname_len - len(value)):
                        my_str += ' '
                if item == 'Age' and len(str(value)) < age_len:
                    k = 0
                    for k in range(int(age_len - len(str(value)))):
                        my_str += ' '
                if item == 'Experience' and len(str(value)) < experience_len:
                    k = 0
                    for k in range(experience_len - int(len(str(value)))):
                        my_str += ' '
                if item == 'Salary' and len(str(value)) < salary_len:
                    k = 0
                    for k in range(salary_len - int(len(str(value)))):
                        my_str += ' '
        my_str += '#'
        print(my_str)

    # Печатаем таблицу
    width = name_len + surname_len + age_len + experience_len + salary_len + 16
    print('#' * width)
    head = {'Name': 'Name', 'Surname': 'Surname', 'Age': 'Age', 'Experience': 'Experience', 'Salary': 'Salary'}
    my_print(head)
    for minidict in my_base:
        print('#' * width)
        my_print(minidict)
    print('#' * width)


def sort():

    def sort_function(my_filter):
        sort_list = []                      # Тут будет список ключевых значений для соритовки
        sorted_base = []                    # Сюда запишем отсортированный список
        global my_base
        for minidict in my_base:
            for item, value in minidict.items():
                if item == 'number':
                    index = value
                if item == my_filter:
                    sort_list.append([value, index])
        sort_list.sort()                    # Получили отсоритованный список по ключевому значению с индексом
        for sort_item in sort_list:
            for minidict in my_base:
                for item, value in minidict.items():
                    if item == 'number':
                        index = value
                    if item == my_filter and sort_item[0] == value and sort_item[1] == index:
                        sorted_base.append(minidict)
        my_base = copy.deepcopy(sorted_base)

    while True:
        print('Sort by: 1: Name, 2: Surname, 3: Age, 4: Experience, 5: Salary.')
        answer = input('Please choose by what basis we will sort:')
        if answer == '1':
            sort_function('Name')
            break
        elif answer == '2':
            sort_function('Surname')
            break
        elif answer == '3':
            sort_function('Age')
            break
        elif answer == '4':
            sort_function('Experience')
            break
        elif answer == '5':
            sort_function('Salary')
            break
        else:
            print('You are entered wrong command. Please enter valid command (1, 2, 3, 4, 5):')
            continue

# Функция проверки является ли введенная информация строкой (состоит только из букв)
def check_str(my_str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if isinstance(my_str, str):
        index = my_str.upper()
        for k in range(len(index)):
            if index[k] in alphabet:
                continue
            else:
                return False


# Функция проверки является ли введенная информация целым числом
def check_int(my_int):
    if str(my_int).isdigit() is True:
        return True
    else:
        return False


waiting_answer()
