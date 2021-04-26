'''
Створіть власну реалізацію вбудованої функції range під назвою in_range(), яка приймає три
параметри: start, end, і опціонально step.
Підказка: перегляньте документацію для функції range.
'''


def in_range(end, start=None, step=1):
    if start is not None:
        first = end
        finish = start
    elif start is None:
        first = 0
        finish = end
    if step < 0:
        while first > finish:
            yield first
            first += step
    else:
        while first < finish:
            yield first
            first += step
