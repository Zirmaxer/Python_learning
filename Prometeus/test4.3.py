import sys

#Объявление переменных
my_list = [""]
my_input=str(sys.argv[1])
a=int(len(my_input))
answer=str(None)

# Перевод строки в список
for my_list in my_input :
    my_list += my_input

# Проверка условия задачи
i=1
k=0
while i < a+1 :
    if my_list[i]=="(":
        k = k+1
        i = i+1
    elif my_list[i]==")":
        k= k-1
        i = i+1
        if k<0:
            break

#Проверка значения k
if k == 0:
  answer="YES"
else:
  answer="NO"

#Вывод результата
print (answer)