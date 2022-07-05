# Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).


from random import shuffle


def shuffle_matrix(__matrix: list[list[int]]) -> list[list[int]]:
    for row in __matrix:
        shuffle(row)
    return __matrix


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

shuffle_matrix(matrix)
print(matrix)
