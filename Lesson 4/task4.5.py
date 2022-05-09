# На вход программе подается число n.
# Напишите программу, которая создает
# и выводит построчно список, состоящий из n списков
# [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].

n = int(input())

result_list = []
for _ in range(n):
    row = [i + 1 for i in range(n)]
    result_list.append(row)

for row in result_list:
    print(row)
