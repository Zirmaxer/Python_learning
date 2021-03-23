my_base = []
def waitingAnswer():
    while True:
        answer = input ('Please enter your joice (create, show, sort, quit) :')
        answer = answer.lower()
        if answer == 'create':
            create()
        elif answer == 'show':
            pass
        elif answer == 'sort':
            pass
        elif answer == 'quit':
            break
        else:
            print ('You are entered wrong command. Please enter valid command (create, show, sort, quit):')
            continue

def create():
    while True:
        name = input('Your name: ')
        if checkStr (name) == False:
            print ('Please reenter your Name (must be only string): ')
            continue
        else:
            my_base.append({'Name': name.capitalize()})
            break
    print(my_base)


def show():
    pass

def sort():
    pass

#Функция проверки является ли введенная информация строкой (состоит только из букв)
def  checkStr(mystr):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if isinstance(mystr, str):
        index = mystr.upper()
        for k in range(len(index)):
            if index[k] in (alphabet):
                continue
            else:
                return False

waitingAnswer()
