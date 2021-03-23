import sys

#Назначение переменных
text = sys.argv
my_text=str("")
answer=str(None)


my_text = ''.join(text[1:])             #Превращаем лист в строку
my_text = my_text.replace(' ', '')      #Убираем пробелы из строки
my_text = my_text.lower()               #Понижаем регистр текста

#Определение, является ли строка палиндромом
x = len(my_text)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if my_text[x - i] == my_text[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  answer="NO"
else:
  answer="YES"

#Вывод результата
print (answer)