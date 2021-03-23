import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])
zz='!' if z>0 else '.'          #Проверка значения z 
#Подсчет количества la
w='la' if x>0 else ' ' 
m=0
while m < x-1:
    w +='-la'
    m=m+1
#Конец подсчета коколичества la
#Подсчет количества куплетов
f=w if y>0 else ' '
m=0
while m < y-1:
    f +=' '
    f += w
    m=m+1
#Конец подсчета количества куплетов
f += zz                         #Добавление окончания в фразу
#Финальная сборка фразы
final='Everybody sing a song:'
final += f
#Вывод ответа
print(final)