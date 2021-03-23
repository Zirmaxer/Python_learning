import sys

n = int (9)
m = int (3)

def super_fibonacci(n, m):
    list_fib = []
    
    #Создаем начало нашего списка
    i = 0
    number = 0
    while i < m:
        list_fib.extend ("1")
        i += 1
    #КОнец

    i = m+1
    while i <= n:
        x=1
        number=0
        while x<(m+1):
            number= number + int(list_fib[i-x-1])
            x += 1
        list_fib.extend ([str(number)])
        i += 1
    counter = (len (list_fib)) - 1
    return int(list_fib[counter])

answer = super_fibonacci (n , m)
print (answer)