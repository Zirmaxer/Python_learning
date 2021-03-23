import sys

my_input = 'SOS, a....'

def encode_morze (text):
    morse_code = {
        "A" : ".-", 
        "B" : "-...", 
        "C" : "-.-.", 
        "D" : "-..", 
        "E" : ".", 
        "F" : "..-.", 
        "G" : "--.", 
        "H" : "....", 
        "I" : "..", 
        "J" : ".---", 
        "K" : "-.-", 
        "L" : ".-..", 
        "M" : "--", 
        "N" : "-.", 
        "O" : "---", 
        "P" : ".--.", 
        "Q" : "--.-", 
        "R" : ".-.", 
        "S" : "...", 
        "T" : "-", 
        "U" : "..-", 
        "V" : "...-", 
        "W" : ".--", 
        "X" : "-..-", 
        "Y" : "-.--", 
        "Z" : "--.."
    }
    output = ''
    code = ''
    text = text.upper()
    size = len (text)
    for item in range (size):
        output = output + morse_code.get (str(text[item]),'')
        latter = morse_code.get (str(text[item]),'')
        latter_size = len (latter)
        for i in range(latter_size):
            if latter[i] == '.':
                code = code + '^'
                if i < latter_size-1:
                    code = code + '_'
            elif latter[i] == '-':
                code = code + '^^^'
                if i < latter_size-1:
                    code = code + '_'
        if item < size-1 and latter!='':
            code = code + '___'
        if text[item] == ' ':
            code = code + '____'
        if item == size-1 and code[-1] == '_':
            code_size = len (code)
            code = code[0:-3:1]
    return code
answer = encode_morze(my_input)
print (answer)