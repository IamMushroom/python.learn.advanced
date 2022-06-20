# Даны по 10-балльной шкале оценки по математике трех учеников. Напишите программу, которая выводит множество оценок, имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников.

def solution(array1: list[int], array2: list[int], array3: list[int]) -> set[int]:
    result = set()
    for number in array1:
        if not(number in array2 and number in array3):
            result.add(number)
    for number in array2:
        if not(number in array1 and number in array3):
            result.add(number)
    for number in array3:
        if not(number in array2 and number in array1):
            result.add(number)
    return result


ar = []
for _ in range(3):
    ar.append([int(num) for num in input().split()])

sol = solution(ar[0], ar[1], ar[2])
for num in range(11):
    if num in sol:
        print(num, end=' ')
