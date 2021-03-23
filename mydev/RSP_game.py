'''
Написать игру в "камень-ножницы-бумага" против компьютера.

Запустить игру в бесконечном цикле. Запросить ввод от пользователя (R - камень, S - ножницы, P - бумага). Сгенерировать случайный выбор компьютера. Вывести выбор компьютера. Определить победителя, выведя соответствующую информацию. Спросить пользователя - хочет ли он повторить игру. Если хочет - повторить, не хочет - выйти из цикла.
'''

import random

answer = 'Y'

print ('Lets play the game "Rock Paper Scissors" ')
while answer == 'Y':
    number = random.randint(1,3)
    if number == 1:
        choise = 'Rock'
    elif number == 2:
        choise = 'Paper'
    else:
        choise = 'Scissors' 
    z = input ('Enter your choise (R = Rock, P = Paper, S = Scissors) :')
    if z == 'R' and number == 1:
        print ('Congratulations! you are the winner!')
        answer = input ('Do you want to play again? ("Y" means yes or "N" means not):')
        if answer == 'Y':
            continue
        else:
           break  
    if z == 'P' and number == 2:
        print ('Congratulations! you are the winner!')
        answer = input ('Do you want to play again? ("Y" means yes or "N" means not):')
        if answer == 'Y':
            continue
        else:
            break  
    if z == 'S' and number == 3:
        print ('Congratulations! you are the winner!')
        answer = input ('Do you want to play again? ("Y" means yes or "N" means not):')
        if answer == 'Y':
            continue
        else:
            break  
    else: 
        print (f"Sorry, you are did'nt gues! My choise was {choise}")
        answer = input ('Do you want to play again? ("Y" means yes or "N" means not):')
        if answer == 'Y':
            continue
        else:
            break   