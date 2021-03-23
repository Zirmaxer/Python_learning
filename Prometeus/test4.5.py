'''
Дешифрувати повідомлення, зашифроване шифром Бекона

Для кодування повідомлень Френсіс Бекон запропонував кожну літеру тексту замінювати на групу з п'яти символів «А» або «B» (назвемо їх "ab-групами"). Для співставлення літер і кодуючих ab-груп в даному завданні використовується ключ-ланцюжок aaaaabbbbbabbbaabbababbaaababaab, в якому порядковий номер літери відповідає порядковому номеру початку ab-групи.
Наприклад: літера "а" - перша літера алфавіту; для визначення її коду беремо 5 символів з ключа, починаючи з першого: aaaaa. Літера "c" - третя в алфавіті, отже для визначення її коду беремо 5 символів з ключа, починаючи з третього: aaabb.
Таким чином, оригінальне повідомлення перетворюється на послідовність ab-груп і може далі бути накладене на будь-який текст відповідної довжини: А позначається нижнім регістром, В - верхнім.
'''

import sys

#Объявление переменных
key = 'aaaaabbbbbabbbaabbababbaaababaab'    #range 31
alphabet = 'abcdefghijklmnopqrstuvwxyz'     #range 25
big_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #range 25
text=(sys.argv)
my_text = str ("")
code = str ("")
input_text = str ("")
uncode_text = str ("")
input_text_len = int ()

#Функция дежифрования строки аааввв
def description (input_text):
    uncode_text = ("")
    input_text_len = len (input_text)
    ii = 0
    while ii < input_text_len :
        i=0
        for i in range(26):
            if input_text[ii] == str(alphabet[i]):
                uncode_text = uncode_text + "a"
                i = i+1
            elif input_text[ii] == str(big_alphabet[i]):
                uncode_text = uncode_text + "b"
                i = i+1
        ii += 1
    return uncode_text  
#Конце функции

#Функция перевода шифра в буквы
def code_to_alphabet (code):
    uncode_text = ""
    input_text_len = len (code)
    ii=0
    while ii <= input_text_len :
        if ii+5 > input_text_len:       #Віходим из кицла если осталось меньше 5 букв в зашифрованом коде
            break
        i=0
        for i in range(26):
            if code[ii:ii+5] == key[i:i+5]:
                uncode_text = uncode_text + str(alphabet[i])
            i += 1
        ii += 5
    return uncode_text
#Конце функции

my_text = "".join(text[1:])             #Превращаем лист в строку
my_text = my_text.replace(' ', '')      #Убираем пробелы из строки
code = description(my_text)             #Дешефруем текст сообщения
answer = (code_to_alphabet(code))       #Получаем дешефрованное слово

print (answer)