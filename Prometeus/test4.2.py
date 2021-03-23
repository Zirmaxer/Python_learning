import sys

text = sys.argv
text.reverse()
a=int(len(sys.argv))
outtext=str("")

i=int(0)
while i < (a-2) :
    outtext = outtext + str(text[i]) + " "
    i = i+1

outtext = outtext + str(text[a-2])
print (outtext)