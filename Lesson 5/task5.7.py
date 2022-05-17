# На шахматной доске 8×8 стоит ферзь.
# Отметьте положение ферзя на доске и все клетки, которые бьет ферзь.
# Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *,
# остальные клетки заполните точками.

n = 8
chessboard = []
figure = 'Q'
filler = '.'
possible_turn = '*'

for i in range(n):
    row = []
    for j in range(n):
        row.append(filler)
    chessboard.append(row)

figure_pos = input()
figure_i = n - int(figure_pos[1])
figure_j = ord(figure_pos[0].lower()) - ord('a')

for i in range(n):
    for j in range(n):
        if i == figure_i or j == figure_j or abs(figure_i - i) == abs(figure_j - j):
            chessboard[i][j] = possible_turn

chessboard[figure_i][figure_j] = figure

for row in chessboard:
    print(*row)
