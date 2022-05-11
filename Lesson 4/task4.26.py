# На шахматной доске 8×8 стоит конь.
# Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь.
# Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.

# Может ли на эту клетку пойти конь?
def is_horse_turn(x1, y1, x2, y2):
    x = x1 - x2
    if x < 0:
        x = x * -1
    y = y1 - y2
    if y < 0:
        y = y * -1
    return (x == 1 and y == 2) or (x == 2 and y == 1)


n = 8
fill = '.'
horse = 'N'
turn_fill = '*'
first_letter = 'a'

# Заполняем доску точками
board = []
for _ in range(n):
    row = []
    for __ in range(n):
        row.append(fill)
    board.append(row)

# Получаем позицию коня
horse_cell = input()
horse_j = ord(horse_cell[0]) - ord(first_letter)
horse_i = 8 - int(horse_cell[1])
board[horse_i][horse_j] = horse

# Проходим по доске и отмечаем все возможные позиции
for i in range(n):
    if i < horse_i - 2:
        continue
    elif i > horse_i + 2:
        break
    else:
        for j in range(n):
            if j < horse_j - 3:
                continue
            elif j > horse_j + 3:
                break
            else:
                if is_horse_turn(horse_i, horse_j, i, j):
                    board[i][j] = turn_fill

# Выводим доску
for row in board:
    print(*row)
