# На вход программе подается строка текста, содержащая символы и число n.
# Из данной строки формируется список.
# Напишите программу, которая разделяет список на вложенные подсписки так, что n последовательных элементов принадлежат разным подспискам.

main_list = [elem for elem in input().split()]
n = int(input())

sublists = []
for _ in range(n):
    sublists.append([])

sublist = 0
for char in main_list:
    sublists[sublist].append(char)
    sublist = (sublist + 1) % n

print(sublists)
