import sys

my_input1=int(sys.argv[1])
my_input2=int(sys.argv[2])
my_list1 = []
my_list2 = []
list_numbers = []
answer=str(None)
index=int(0)

while my_input1 <= my_input2 :
    input1 = str (my_input1)
    a = len (input1)
    if a==1:
        temp = [0,0,0,0,0,int(input1[0])]
    elif a==2:
        temp = [0,0,0,0,int(input1[0]),int(input1[1])]
    elif a==3:
        temp = [0,0,0,int(input1[0]),int(input1[1]),int(input1[2])]
    elif a==4:
        temp = [0,0,int(input1[0]),int(input1[1]),int(input1[2]),int(input1[3])]
    elif a==5:
        temp = [0,int(input1[0]),int(input1[1]),int(input1[2]),int(input1[3]),int(input1[4])]
    elif a==6:
        temp = [int(input1[0]),int(input1[1]),int(input1[2]),int(input1[3]),int(input1[4]),int(input1[5])]
    # Проверка счастливого номера
    if (int(temp[0]+temp[1]+temp[2]))==(int(temp[3]+temp[4]+temp[5])):
        index += 1
        list_numbers.append(temp) 
    my_input1 += 1

print (index)