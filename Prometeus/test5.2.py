'''
Розробити функцію counter(a, b), 
яка приймає 2 аргументи -- цілі невід'ємні числа a та b, 
та повертає число -- кількість різних цифр числа b, які містяться у числі а.
'''

import sys

my_list = [123, 451]
answer = int (0)

def counter(a, b):
    list_b = list (str(b))
    list_a = list (str(a))
    #подфункция убирающая дубли значений в списке
    def clean_list(list_to_clean) :
        def clean (number,list_to_clean):
            size_list = len (list_to_clean)
            clear_list = []
            i = number + 1
            x = number
            while i < (size_list) :
                if ((list_to_clean[x] == list_to_clean[i])) and (type(list_to_clean[x]) == type (list_to_clean[i])):
                    clear_list.extend([i])
                    i = i+1
                else:
                    i = i+1
            size_list = len (clear_list)
            i = 0
            k = 0
            while i <= (size_list-1):
                del list_to_clean[(clear_list[i]-k)]
                k = k+1
                i = i+1
            return list_to_clean
        size_list = len (list_to_clean)
        i = 0
        while i < (size_list-1):
            list_to_clean = clean (i,list_to_clean)
            i = i+1
        return list_to_clean    
    #конец функции
    
    list_a = clean_list (list_a)        # убираем дубли в числе a
    list_b = clean_list (list_b)        # убираем дубли в числе b
    
    size_a = len(list_a)
    size_b = len(list_b)

    # запускаем цикл сравнения цифр и увеличиваем счетчик answer при совпадении
    answer = int (0)
    x = 0
    while x < (size_b):
        i = 0
        while i < (size_a):
            if list_a[i] == list_b[x]:
                answer = answer + 1
                i = i+1
            else:
                i = i+1    
        x = x+1
    return answer

answer = counter (my_list[0], my_list[1])
print (answer)