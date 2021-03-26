my_base = []


def waiting_answer():
    while True:
        answer = input('Please enter your joice (create, show, sort, quit) :')
        answer = answer.lower()
        if answer == 'create':
            create()
        elif answer == 'show':
            show()
        elif answer == 'sort':
            pass
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
        age = int(input('Please enter your age: '))
        if check_int(age) is False or age < 0 or age > 150:
            print('Please reenter your age (must be integer (min 1, max 150): ')
            continue
        else:
            break

    # Запрашиваем стаж
    while True:
        experience = int(input('Please enter your experience: '))
        if check_int(experience) is False or experience > age:
            print('Please reenter your experience (must be integer (less than age): ')
            continue
        else:
            break

    # Запращиваем уровень зарплаты
    while True:
        salary = int(input('Please enter your level of salary: '))
        if check_int(salary) is False or salary < 0:
            print('Please reenter your level of salary (must be integer (more than zero): ')
            continue
        else:
            break

    # Записываем данные в my_base
    my_base.append({'Name': name.capitalize(), 'Surname': surname.capitalize(), 'Age': age, 'Experience': experience,
                    'Salary': salary})


def show():
    print(my_base)


def sort():
    pass


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
