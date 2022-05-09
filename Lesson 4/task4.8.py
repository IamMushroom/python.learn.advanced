# На вход программе подается натуральное число n.
# Напишите программу, которая выводит
# первые n строк треугольника Паскаля.

from math import factorial


def pascal(num):
    result_list = []
    if num == 0:
        result_list = [1]
    elif num == 1:
        result_list = [1, 1]
    else:
        for i in range(num + 1):
            elem = factorial(num) / (factorial(i) * factorial(num - i))
            result_list.append(int(elem))
    return(result_list)


n = int(input())

pascal_triangle = []
for i in range(n):
    pascal_triangle.append(pascal(i))

for row in pascal_triangle:
    print(*row)
