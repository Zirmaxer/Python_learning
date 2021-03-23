'''
Реализуйте одну классическую и достаточно простую игру: "угадай число".

Компьютер загадывает число от 1 до 50 и даёт 6 попыток пользователю, чтобы тот смог угадать загаданное число. Когда пользователь вводит число, компьютер проверяет угадано ли число и если не угадано, то сообщает пользователю меньше ли или больше загаданое число. Если пользователь угадал - то сообщает о том, что число отгадано.
'''

import random
number = random.randint(1,50)
control = False

for k in range(6):
    z = int( input ('Please, enter the number:'))
    if z == number:
        print ('You did it!')
        control = True
        break
    if number > z:
        print (f'The sicret number is more than {z}')
        continue
    if number < z:
        print (f'The sicret number is less than {z}')
        continue
if control == False:
    print ("Sorry, you are use your six attempts and did'nt got the number")
    print (number)