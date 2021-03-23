import sys

my_x = 'ZZZZ'
my_n = 36
my_m = 13

def convert_n_to_m(x, n, m):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Проверяем является ли х числом ли строкой + проверка на отрицательное число
    if isinstance(x, (float, list, bool, set, type)):
        return False
    elif isinstance(x, int) and x<0:
        return False
    if isinstance(x, str):
        index = x.upper()
        for k in range(len(index)):
            if index[k] in (alphabet[0:n]):
                continue
            else:
                return False
    # конец проверки
    
    #Конвертируем число в десятичную систему исчисления
    num = str (x)
    num = num.upper()                       
    num_10 = int (num, n)  
    #Переводим число в систему исчесления m
    if m == 1:
        return '0'* num_10
    def convert(num, to_base=10, from_base=10):
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        if n < to_base:
            return alphabet[n]
        else:
            return convert (n // to_base, to_base) + alphabet[n % to_base]
    return convert(num_10, to_base=m, from_base=10)
answer = convert_n_to_m(my_x, my_n, my_m)
print (answer)