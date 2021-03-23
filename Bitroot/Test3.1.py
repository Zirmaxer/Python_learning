import random
random_list = []
i = 0
while i < 10:
    random_list.append(random.randint(0, 1000))
    i += 1
biggest_element = random_list[0]
i = 1
while i < 10:
    if random_list[i] > biggest_element:
        biggest_element = random_list[i]
        i += 1
    else:
        i += 1
        continue
print(biggest_element)
