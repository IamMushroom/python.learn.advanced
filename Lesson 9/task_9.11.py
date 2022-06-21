# Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников присутствовал на всех уроках с начала учебного года.
# Для каждого урока есть листок со списком присутствовавших учеников.
#
# Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.

n = int(input())
m = int(input())
prev_students = {input() for __ in range(m)}
for _ in range(n - 1):
    m = int(input())
    students = {input() for __ in range(m)}
    prev_students.intersection_update(students)

print(*sorted(prev_students), sep='\n')
