# На вход программе подаются две строки,
# на одной символы, на другой число n.
# Из первой строки формируется список.
# Реализуйте функцию chunked(),
# которая принимает на вход список и число,
# задающее размер чанка (куска),
# а возвращает список из чанков указанной длины.

def chunked(string, count):
    string_list = string.split()
    result_list = []

    while len(string_list) > count:
        row = []
        for _ in range(count):
            row.append(string_list[0])
            del string_list[0]
        result_list.append(row)

    row = []
    while len(string_list) > 0:
        row.append(string_list[0])
        del string_list[0]
    result_list.append(row)

    return result_list


st = input()
n = int(input())

print(chunked(st, n))
