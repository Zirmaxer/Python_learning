import random
import sys

ALLOWED_GAME_MODES = {'beginner', 'medium', 'expert'}
PREDEFINED_MODES = {
    'beginner': (8, 8, 10),
    'medium': (16, 16, 40),
    'expert': (16, 30, 99),
}


def generate_maze(max_rows, max_cols, max_mines):
    #функция случайной генерации координат мин
    def generate_mines(max_rows, max_cols, max_mines):
        i = 1
        mines = []
        while i < max_mines:
            number1 = random.randint(0, max_rows - 1)
            number2 = random.randint(0, max_cols - 1)
            if len(mines) == 0:
                mines.append([number1, number2])
            else:
                for k in mines:
                    if k[0] == number1 and k[1] == number2:
                        break
                    elif k == mines[-1]:
                        mines.append([number1, number2])
                        i += 1
                    else:
                        continue
        return mines
    mines = generate_mines(max_rows, max_cols, max_mines) #мы получили список координат мин
    #генерируем пустое минное поле
    mine_field = [[0 for l in range(max_rows)] for l in range(max_cols)]
    #функция вставки чисел на минном поле
    def set_number_on_field(x, y):
        if x < 0 or x > max_rows-1 or y < 0 or y > max_cols-1:
            pass
        elif mine_field[y][x] == -1:
            pass
        else:
            mine_field[y][x] += 1
    #функция расстановки мин и чисел на поле
    def input_mines_on_field(mines):
        for k in mines:
            mine_field[k[1]][k[0]] = -1
            coordinates_x = k[0]
            coordinates_y = k[1]
            set_number_on_field(coordinates_x - 1, coordinates_y - 1)
            set_number_on_field(coordinates_x, coordinates_y - 1)
            set_number_on_field(coordinates_x + 1, coordinates_y - 1)
            set_number_on_field(coordinates_x - 1, coordinates_y)
            set_number_on_field(coordinates_x + 1, coordinates_y)
            set_number_on_field(coordinates_x - 1, coordinates_y + 1)
            set_number_on_field(coordinates_x, coordinates_y + 1)
            set_number_on_field(coordinates_x + 1, coordinates_y + 1)

    input_mines_on_field(mines)
    return mine_field

def print_maze(maze_matrix):
    for i in range(len(maze_matrix)):
        for j in range(len(maze_matrix[0])):
            item = "*" if maze_matrix[i][j] == -1 else str(maze_matrix[i][j])
            print(item, end=' ')
        print()


def main(mode='beginner'):
    print_maze(generate_maze(*PREDEFINED_MODES[mode]))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('Only one parameter is allowed.')

    game_mode = sys.argv[1]
    if game_mode not in ALLOWED_GAME_MODES:
        raise ValueError('Only beginner, medium and expert models are allowed')

    main(game_mode)
