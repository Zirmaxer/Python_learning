number = '69L'

def count_holes(n):
    my_dict = {'0':1, '1':0, '2':0, '3':0, '4':1, '5':0, '6':1, '7':0, '8':2, '9':1}
    if type(n)== int:      
        my_number = str(n)
        summ = 0
        size = len (my_number)
        for item in range(size):
            summ = summ + my_dict.get(str(my_number[item]),0)
        return summ
    elif type(n) == str:
        if n.isdigit() == False:
            return 'ERROR'
        else:
            tmp = int(n)
            my_number = str(tmp)
            summ = 0
            size = len (my_number)
            for item in range(size):
                summ = summ + my_dict.get(str(my_number[item]),0)
            return summ
    else:
        return 'ERROR'

answer = count_holes(number)
print (answer)