import random
first_list = []
second_list = []
stdout = []
i = 0
while i < 10:
    first_list.append(random.randint(1, 10))
    second_list.append(random.randint(1, 10))
    i += 1
list1 = set(first_list)
list2 = set(second_list)
stdout = list1.intersection(list2)
stdout = list(stdout)
print(stdout)