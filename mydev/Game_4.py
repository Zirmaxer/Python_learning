print ('''
Предлагаю древнюю китайскую игру в палочки.
Играют два игрока.  Есть 10 палочек. 
Игроки по очереди берут от одной до трёх палочек. 
Играют до тех пор пока не закончатся палочки. 
Тот кто взял последним - тот проиграл.''')

#Вводим имена игроков
player1 = input ('Введите имя первого игрока:') 
player2 = input ('Введите имя первого игрока:') 
if player1 == '' or player2 == ' ':
    player1 = 'player1'
    player2 = 'player2'
stics = 10
print ('Начинаем игру!')
while stics > 0:
    print (f'Сейчас в игре: {stics} игровых палочек')
    player = player1
    print (f'Ход игрока {player1}.')
    now = int(input ('Сколько палочек вы забираета (от 1 до 3х)?:'))
    if now > 3 or now < 1:
        print ('Взять можно от 1 до 3х палочек. Повторите ввод!')
        now = int(input ('Сколько палочек вы забираета (от 1 до 3х)?:'))
    stics -= now
    print (f'Сейчас в игре: {stics} игровых палочек')
    player = player2
    print (f'Ход игрока {player2}.')
    now = int(input ('Сколько палочек вы забираета (от 1 до 3х)?:'))
    if now > 3 or now < 1:
        print ('Взять можно от 1 до 3х палочек. Повторите ввод!')
        now = int(input ('Сколько палочек вы забираета (от 1 до 3х)?:'))
    stics -= now
if player == player1:
    winner = player2
else:
    winner = player1    
print (f'Игра окончена! Поздравляем, {winner} выиграл')
    