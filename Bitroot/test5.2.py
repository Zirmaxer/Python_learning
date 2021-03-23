def create_file(file_name):
    with open (file_name, 'w') as my_file:
        my_file.write('Hello file world!\n')
    my_file.close


def read_file(file_name):
    with open (file_name, 'r') as my_file:
        text = my_file.read()
    my_file.close
    return text

create_file('myfile.txt')
print(read_file('myfile.txt'))