# Напишите программу, которая проверяет,
# является ли заданная квадратная матрица магическим квадратом.

# Проверяем, что все суммы равны
def is_valid_sum(matrix):
    matrix_len = len(matrix[0])
    matrix_sum = sum(matrix[0])
    main_diag = []
    add_diag = []

    for i in range(matrix_len):
        if sum(matrix[i]) == matrix_sum:
            for j in range(matrix_len):
                if j == i:
                    main_diag.append(matrix[i][j])
                if j == matrix_len - 1 - i:
                    add_diag.append(matrix[i][j])
        else:
            return False

    for j in range(matrix_len):
        summ = 0
        for i in range(matrix_len):
            summ += matrix[i][j]
        if summ != matrix_sum:
            return False

    if matrix_sum == sum(main_diag) and matrix_sum == sum(add_diag):
        return True
    else:
        return False

# Проверяем, что матрица состоит из всех чисел от 0 до n ** 2


def is_valid_numbers(matrix):
    numbers = []

    for row in matrix:
        for num in row:
            numbers.append(num)

    numbers.sort()
    if numbers[0] != 1:
        return False
    else:
        for i in range(len(numbers) - 2):
            if numbers[i + 1] != numbers[i] + 1:
                return False

    return True


# Вводим данные
n = int(input())
matrix = []
for i in range(n):
    row = [int(j) for j in input().split()]
    matrix.append(row)

# Проверяем выполнение условий
if is_valid_numbers(matrix) and is_valid_sum(matrix):
    result = 'YES'
else:
    result = 'NO'

# Выводим результат
print(result)
