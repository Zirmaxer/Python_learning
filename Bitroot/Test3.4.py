sentence = "Some random sentence random randome"
# write your program here
sentence = sentence.lower()
data = sentence.split(' ')
my_dict = dict()
for item in data:
    my_dict[item]=data.count(item)
print (my_dict)