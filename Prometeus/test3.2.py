import sys
from colorama import init
init()
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

answer=int(0)
element1=0
element2=1

#Функция считывания данных от пользователя
def text_promt(msg):
    try:
      return raw_input(msg)
    except NameError:
      return input(msg)
# Конец функции считывания данных от пользователя

print (Back.GREEN)
print (Fore.RED)

n=int(text_promt('Введите число n : '))
#Проверяем значение на отрицательное, 0 или 1
if n<0:
    print ('n can not be a negative number')
elif n==0:
    answer=0    
elif n==1:
    answer=1
else:
    i=0
    while i<(n-1):
        element3=element2
        element2=element1+element2
        element1=element3
        answer=element2
        i=i+1
print (answer)