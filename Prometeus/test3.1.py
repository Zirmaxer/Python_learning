import sys
a=float(sys.argv[1])
b=float(sys.argv[2])
c=float(sys.argv[3])
answer='zero'
# Проверка значений длины стороны
answer='not triangle' if a<0.001 else answer            #Проверка значения a 
answer='not triangle' if b<0.001 else answer            #Проверка значения b 
answer='not triangle' if c<0.001 else answer            #Проверка значения c 
# Конец проверки значений длины стороны
# Нахождение большей и меньших сторон
if answer=='zero':
    bigest_side=a 
    midle_side1=b  
    midle_side2=c                              
    if b>a:
        bigest_side=b
        midle_side1=a
        midle_side2=c
    elif c>a:
        bigest_side=c
        midle_side1=a
        midle_side2=b
    answer='triangle' if (midle_side1+midle_side2)>bigest_side else 'not triangle' #Проверка возможности сложить трехугольник
    print (answer)
else:
    answer='not triangle'
    print (answer)