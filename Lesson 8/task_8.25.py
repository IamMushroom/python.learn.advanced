# Даны по 10-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.

def solution(array1: list[int], array2: list[int], array3: list[int]) -> set[int]:
    result = set()
    for number in array3:
        if not(number in array2 or number in array1):
            result.add(number)
    return result


ar = []
for _ in range(3):
    ar.append([int(num) for num in input().split()])

sol = solution(ar[0], ar[1], ar[2])
for num in range(10, -1, -1):
    if num in sol:
        print(num, end=' ')
