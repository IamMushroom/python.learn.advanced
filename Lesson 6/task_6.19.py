# Напишите программу, которая выводит список хорошистов и отличников в классе.

n = int(input())
students = ()
for _ in range(n):
    students += tuple([i for i in input().split()])

good_students = []
for i in range(1, len(students), 2):
    if int(students[i]) >= 4:
        good_students.append(students[i - 1])
        good_students.append(students[i])

for i in range(1, len(students), 2):
    print(f'{students[i - 1]} {students[i]}')

print()

for i in range(1, len(good_students), 2):
    print(f'{good_students[i - 1]} {good_students[i]}')
