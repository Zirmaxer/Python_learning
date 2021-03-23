def MyInputInteger ():
    while True:
        try:
            number_of_words = int(input('Please, enter number of words in the sentence:'))
            return number_of_words
        except:
            print('Not an integer number. Try again!')
            continue
    return number_of_words

a = MyInputInteger()
print(a)