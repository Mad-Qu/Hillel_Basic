import stock_maze  # файл stock_maze.py с лабиринтом (список maze)


# разбирает строки(значения "m") на символы в списке строк (n * m)
# так как лабиринт подается в формате списка строк
def do_symbol_list(maze_list: list) -> list:
    result_list = []
    index = 0

    for line in maze_list:
        result_list.append([symbol for symbol in maze_list[index][0]])
        index += 1

    return result_list


# Ищем потенциальные точки выхода - символ "." по периметру лабиринта
# складываем их в список списков в формате [[m1, n1], [m2, n2] ... [m_x, n_x]]
def do_search_potential_exit(maze_list: list) -> list:
    potential_exit_list = []
    index = 0
    for value in maze_list[0]:
        if value == '.':
            potential_exit_list.append([0, index])
        index += 1

    index = 0
    for value in maze_list[len(maze_list) - 1]:
        if value == '.':
            potential_exit_list.append([len(maze_list) - 1, index])
        index += 1

    for index in range(1, len(maze_list[0]) - 1):
        if maze_list[index][0] == '.':
            potential_exit_list.append([index, 0])

    for index in range(1, len(maze_list[0]) - 1):
        if maze_list[index][len(maze_list[0]) - 1] == '.':
            potential_exit_list.append([index, len(maze_list) - 1])

    return potential_exit_list


# функция перебором смотрит в каждую клетку лабиринта,
# находит переданное ей число step_count ()
# и если это возможно раздает соседям (← → ↑ ↓) кроме стен значение +1
def do_next_step(symbol_list, step_count):
    length_n = len(symbol_list)
    length_m = len(symbol_list[0])

    for n in range(length_n):

        for m in range(length_m):

            if str(symbol_list[n][m]) == str(step_count):

                try:
                    if symbol_list[n - 1][m] == '.':
                        symbol_list[n - 1][m] = step_count + 1
                except IndexError:
                    pass

                try:
                    if symbol_list[n + 1][m] == '.':
                        symbol_list[n + 1][m] = step_count + 1
                except IndexError:
                    pass

                try:
                    if symbol_list[n][m - 1] == '.':
                        symbol_list[n][m - 1] = step_count + 1
                except IndexError:
                    pass

                try:
                    if symbol_list[n][m + 1] == '.':
                        symbol_list[n][m + 1] = step_count + 1
                except IndexError:
                    pass

    return symbol_list


def do_search_exit(maze: list, x: int, y: int) -> list:

    maze = do_symbol_list(maze)  # переделываем строки лабиринта в символы
    maze[x][y] = 0  # ставим ноль в стартовую позицию
    temp_exit_lst = do_search_potential_exit(maze)  # ищем дырки в периметре
    exit_list = []  # сюда складываем настоящие точки выхода

    for count in range(len(temp_exit_lst)):
        step = 0
        temp_maze = maze[:]

        while (temp_maze[temp_exit_lst[count][0]][temp_exit_lst[count][1]]) == '.' \
                and step < len(temp_maze) * len(temp_maze[0]):
            temp_maze = do_next_step(temp_maze, step)
            step += 1

        if temp_maze[temp_exit_lst[count][0]][temp_exit_lst[count][1]] != '.':
            exit_list.append(temp_exit_lst[count])

    return exit_list


# Если точка старта находится на периметре лабиринта
# то она не расценивается как выход!!!

my_maze = stock_maze.maze2  # для удобства вынес лабиринт в отдельный файл

# на вход лабиринт и координаты старта
# возвращает список списков координат выхода(ов) в формате [x, y]
# или пустой список если нет выхода
points = do_search_exit(my_maze, 1, 0)

for count in range(len(points)):
    print(f'Точка выхода № {count + 1} - {points[count]}')

if not len(points):
    print('Похоже Вы тут на долго, выход не найден :(')