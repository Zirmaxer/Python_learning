'''
Створіть Python-функцію під назвою tree, яка приймає рядок зі шляхом до якоїсь директорії
першим позиційним аргументом і виводить через print її загальну структуру з додатковою інформацією
про розмір усіх файлів. Наприклад,
.
├──inner_dir
│
└──sample (4 bytes)
└──sample (4 bytes)
Якщо отриманий аргумент – не рядок, що веде до директорії, ваш код має викликати ValueError.

tree = os.walk('/Users/andrii.kushnir/Desktop/python scripts')
mytree = list(tree)[0]
print(mytree)
'''


import os

SPLIT = "│  "
END_SPLIT = "   "
TOKEN = "├──"
END_TOKEN = "└──"


def tree(path, padding=''):
    if not os.path.isdir(path):
        raise ValueError('No such directory')
    my_tree = list(os.walk(path))[0]

    # Рисуем дерево папок и файлов
    print('.')
    # Папки
    for item in my_tree[1]:
        draw = ''
        if item == my_tree[1][-1] and len(my_tree[2]) == 0:
            draw += END_TOKEN + item
        else:
            draw += TOKEN + item
        print(draw)
        if item == my_tree[1][-1] and len(my_tree[2]) != 0:
            print(SPLIT)
    # Файлы
    if len(my_tree[2]) != 0:
        for item in my_tree[2]:
            draw = ''
            way = f'{my_tree[0]}/{item}'
            if item == my_tree[2][-1]:
                draw += END_TOKEN + item + ' (' + str(os.path.getsize(way)) + ' bytes)'
            else:
                draw += TOKEN + item + ' (' + str(os.path.getsize(way)) + ' bytes)'
            print(draw)


if __name__ == "__main__":
    tree('/Users/andrii.kushnir/Desktop/python scripts')
