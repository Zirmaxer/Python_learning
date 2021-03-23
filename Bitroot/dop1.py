import random
mylist = ['Andrii', 'name', 'cat', 'BUBLIK', 'the', 'end', 'hello']

#функция для запроса целого числа, для формирования случайного предложения
def get_int():
    while True:
        try:
            number_of_words = int(input('Please, enter number of words in the sentence:'))
            return number_of_words
        except:
            print('Not an integer number. Try again!')
            continue
#запрашиваем у пользователя целое число
number_of_words = get_int()
#создаем предложение из случайных слов в количесве слов, заданных пользователем
user_sentence = ''
i=0
while i < number_of_words:
    tmp = random.randrange(0,6)
    user_sentence = user_sentence + mylist[tmp]
    if i+1 < number_of_words:
        user_sentence += ' '
    i += 1
user_sentence += '.'
user_sentence = user_sentence.capitalize()
print (user_sentence)

#Блок кода по расчету % слов в предложении
user_sentence = user_sentence.replace('.', '')  #удалили точку из предложения
user_sentence = user_sentence.lower()           #нижний регистр предложения
words = user_sentence.split(' ')
myset = set(words)

#блок кода, выводящий % слов в предложении
number = 1
for item in myset:
    percent = user_sentence.count(str(item))/number_of_words*100
    print (f'Word number {number} is {item}, and it takes {percent:.2f} %')
    number += 1
