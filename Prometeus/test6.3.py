'''
Розробити функцію saddle_point(matrix), 
яка приймає 1 аргумент -- прямокутну матрицю цілих чисел, задану у вигляді списка списків, 
та повертає тьюпл із координатами "сідлової точки" переданої матриці або логічну константу False, якщо такої точки не існує.

Сідловою точкою вважається такий елемент матриці, який є мінімальним (строго менше за інші) у своєму рядку та максимальним (строго більше за інші) у своєму стовпці, наприклад:
матриця:
1 2 3
0 2 1
"1" в лівому верхньому кутку (за координатами (0;0)) є сідловою точкою матриці.

Вважати, що передані дані є коректними, тобто матриця не містить інших значень крім цілих чисел, а всі вкладені списки мають однакову довжину. Результуючий тьюпл містить два числа -- порядкові номери сідлової точки в рядку (індекс його списка у зовнішньому списку) та в стовпці (індекс у внутрішньому списку).

Наприклад
1 2 3
3 2 1
Виклик функції: saddle_point([[1,2,3],[3,2,1]])
Повертає: False
8 3 0 1 2 3 4 8 1 2 3
3 2 1 2 3 9 4 7 9 2 3
7 6 0 1 3 5 2 3 4 1 1
Виклик функції: saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]])
Повертає: (1, 2)
21
Виклик функції: saddle_point([[21]])
Повертає: (0, 0)
'''

import sys

my_matrix = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]]
answer = tuple ()
def saddle_point(matrix):
    winner = []
#    if len(matrix)==1 and len (matrix[0])==1:
#        winner.append(0)
#        winner.append(0)
    for i in range(len(matrix)):
        for k in range (len (matrix[i])):
            if k == 0:
                double = 0
                small = int (matrix[i][k])
                myindex_k = k
                myindex_i = i
            if k > 0:
                if int(matrix[i][k]) < small:
                    small = int (matrix[i][k])
                    myindex_k = k
                    myindex_i = i
                if int(matrix[i][k]) == small and k!=myindex_k:
                    double = 1
#                    print ('double is on')
            if k == len(matrix[i])-1:
#                print (small)
 #               print (myindex_i, myindex_k)
                biggest = small
                biggest_z = myindex_i
                if double == 0:
                    for z in range (len(matrix)):
                        if int(matrix[z][myindex_k]) > small and z != myindex_i:
                            biggest = int(matrix[z][myindex_k])
                            biggest_z = z
                        if z == len(matrix)-1:
#                            print ('test')
#                            print (biggest)
#                            print (myindex_i, biggest_z, '\n')
                            if biggest >= small and biggest_z == myindex_i:
                                winner.append(myindex_k)
                                winner.append(biggest_z)
#    print (winner)
#    print (len(matrix))
    if winner == []:
        return False
    else:
        winner = tuple (winner)
        return winner                                   
    

answer = saddle_point (my_matrix)
print ('\nAnswer is :', answer)