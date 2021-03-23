import sys

my_text = str ('hello helllo helo hello')
answer = []

def find_most_frequent(text):
    # Проверяем не пустой ли text
    if text=='':
        return text
    #Блок кода, который переносит все слова в строке в список answer
    my_text = text.lower()
    size = len (my_text)
    word = ''
    answer = []
    for i in range (size):
        if my_text[i]==',' or my_text[i]=='.' or my_text[i]==':' or my_text[i]==';' or my_text[i]=='!' or my_text[i]=='?' or my_text[i]=='-' or my_text[i]==' ':
            if word != '':
                answer.append (word)
                word = ''
        else:
            word = word + my_text[i]
            if i == size-1 and word != '':
                answer.append (word)
    #конец проверки строки на слова, получен список слов в переменной answer
    #проверяем есть ли слова, повторяющиеся в тексте
    our_words=[]
    our_words.append(answer[0])
    size = len(answer)
    for i in range(size):
        for k in range(size):
            if i!=k:    
                if answer[i] == answer[k]:
                    size_out = len(our_words) 
                    index=0                  
                    for y in range(size_out):
                        if answer[i]==our_words[y]:
                            index = 1
                        if y==(size_out-1) and index == 0:
                            our_words.append(answer[i])
    our_words.sort()
    return our_words
        
answer = find_most_frequent(my_text)
print (answer)
print(find_most_frequent(''))