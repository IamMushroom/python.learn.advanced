# На вход программе подается число n.
# Напишите программу, которая создает и выводит построчно
# вложенный список, состоящий из n списков
# [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].

n = int(input())
result_list = []

for i in range(n):
    row = [j + 1 for j in range(i + 1)]
    result_list.append(row)

for row in result_list:
    print(row)
