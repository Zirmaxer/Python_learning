'''
Напишіть Python-функцію inspector, яка визначає корисну інформацію в переданому їй об'єкті
функції та створює читабельний рядок з цією інформацією в такому форматі:

Func name: {func_name}
Func docs: {func_doc_string}
Num of local variables: {num_of_local_variables}
Name of local variables: {local_variable_names}
'''


def inspector(func):
    func_name = func.__name__
    func_doc_string = func.__doc__
    tmp = func.__code__.co_varnames
    local_variable_names = ''
    num_of_local_variables = 0
    for item in tmp:
        local_variable_names += item
        num_of_local_variables += 1
        if item != tmp[-1]:
            local_variable_names += ', '

    return f'Func name: {func_name}\nFunc docs: {func_doc_string}\nNum of local variables: {num_of_local_variables}\nName of local variables: {local_variable_names}\n'
