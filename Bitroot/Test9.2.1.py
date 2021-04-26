'''
Створіть власну реалізацію вбудованої функції enumerate під назвою with_index, яка приймає два
параметри: iterable і start, за замовчуванням 0.
Підказка: перегляньте документацію для функції enumerate.
'''


def with_index(iterable, start=0):
    import itertools as it
    return list(zip(it.count(start=start), iterable))