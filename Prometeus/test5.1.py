'''
Розробити функцію clean_list(list_to_clean), 
яка приймає 1 аргумент -- список будь-яких значень (рядків, цілих та дійсних чисел) довільної довжини, 
та повертає список, який складається з тих самих значень, але не містить повторів елементів. Це значить, що у випадку наявності значення в початковому 
списку в кількох екземплярах перший "екземпляр" значення залишається на своєму місці, а другий, третій та ін. видаляються.
'''

import sys
my_list = ['qwe', 'reg', 'qwe', 'REG']
answer = [""]

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

answer = clean_list(my_list)
print (answer)