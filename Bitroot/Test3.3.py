my_list = [i for i in range(1, 101)]
stdout = []
i = 0
while i < 100:
    if my_list[i] % 7 == 0 and my_list[i] % 5 != 0:
        stdout.append(my_list[i])
    i += 1
print(stdout)
