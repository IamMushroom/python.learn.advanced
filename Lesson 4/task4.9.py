# На вход программе подается строка текста, содержащая символы.
# Напишите программу, которая упаковывает последовательности
# одинаковых символов заданной строки в подсписки.

chars = input().split()
chars_list = []

for char in chars:
    chars_list.append([char])

i = 1
while i < len(chars_list):
    if chars_list[i - 1][0] == chars_list[i][0]:
        chars_list[i - 1].append(chars_list[i][0])
        del chars_list[i]
        continue
    else:
        i += 1

print(chars_list)
