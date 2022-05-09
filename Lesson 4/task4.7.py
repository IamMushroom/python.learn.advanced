# На вход программе подается число n.
# Напишите программу, которая возвращает указанную строку
# треугольника Паскаля в виде списка
# (нумерация строк начинается с нуля).

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

print(pascal(n))
