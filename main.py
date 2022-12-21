# table  - матрица для записи ходов
# inversion_table инверсия матрицы, для реализации проверки на победу
# find_winner - переменная счетчик для прекращения игры в случае победы
# sign - знак х или о для определения победителя
# tic_tac_give(place, sign) функция для заполнения матрицы  table
# write_coordinate(sign) функция ввода ходов
# print_table(val)  функция для рисования поля игры
# line_check_func(tables, sign)  функция для построчной проверки массива на совпадение значений(победу)
# winner_func(sign) функция проверки на победу и инверсии матрицы
table = [["-" for x in range(3)] for y in range(3)]
inversion_table = [["-" for u in range(3)] for g in range(3)]
find_winner = ""


def tic_tac_give(place, sign):
    global find_winner
    if (0 <= place[0] <= 2) and (0 <= place[1] <= 2):
        if table[place[0]][place[1]] == "-":
            if sign == "x":
                table[place[0]][place[1]] = "x"
                find_winner = winner_func(sign)
            else:
                table[place[0]][place[1]] = "o"
                find_winner = winner_func(sign)
        else:
            print("This place busy, please write others coordinate")
            write_coordinate(sign)
    else:
        print("Error coordinate, please write others coordinate")
        write_coordinate(sign)


def write_coordinate(sign):
    player = list(map(int, input(f"Player write coordinate {sign}: ").split()))
    tic_tac_give(player, sign)


def print_table(val):
    print("\t")
    print('\t   |  0  |  1  |  2  |')
    print('\t   |_____|_____|_____|')
    print("\t   |     |     |     |")
    print("\t0  |  {}  |  {}  |  {}  |".format(val[0][0], val[0][1], val[0][2]))
    print('\t   |_____|_____|_____|')

    print("\t   |     |     |     |")
    print("\t1  |  {}  |  {}  |  {}  |".format(val[1][0], val[1][1], val[1][2]))
    print('\t   |_____|_____|_____|')

    print("\t   |     |     |     |")
    print("\t2  |  {}  |  {}  |  {}  |".format(val[2][0], val[2][1], val[2][2]))
    print("\t   |     |     |     |")


def line_check_func(tables, sign):
    for row in tables:
        if row[0] == row[1] == row[2] and row[0] != "-":
            return sign


def winner_func(sign):
    checks_stop = line_check_func(table, sign)
    if checks_stop is not None:
        return sign
    for m in range(3):
        for j in range(3):
            inversion_table[j][m] = table[m][j]
    checks_stop = line_check_func(inversion_table, sign)
    if checks_stop is not None:
        return sign

    if ((table[0][0] == table[1][1] == table[2][2] and table[1][1] != "-")
            or (table[0][2] == table[1][1] == table[2][0] and table[1][1] != "-")):
        return sign

    return ""


print_table(table)
name_first_player = input("Write the name player which play for 'x' please: ")
name_second_player = input("Write the name player which play for 'o' please: ")
for i in range(9):
    if find_winner == "":
        if i % 2 == 0:
            signs = "x"
        else:
            signs = "o"
        write_coordinate(signs)
        print_table(table)
    elif find_winner == "x":
        print_table(table)
        print(f"The player {name_first_player}, who played for {find_winner}, won! ")
        break
    else:
        print_table(table)
        print(f"The player {name_second_player}, who played for {find_winner}, won! ")
        break

    if find_winner == "" and i == 8:
        print_table(table)
        print(f"Draw, friendship wins ")

