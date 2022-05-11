# На вход программе подается строка текста,
# содержащая символы. Из данной строки формируется список.
# Напишите программу, которая выводит список,
# содержащий все возможные подсписки списка,
# включая пустой список.

st = input().split()

result_list = [[]]
for i in range(len(st) - 1):
    for j in range(len(st) - i):
        row = []
        for k in range(i + 1):
            row.append(st[j + k])
        result_list.append(row)

result_list.append(st)
print(result_list)
