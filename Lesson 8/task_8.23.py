# Даны по 1010-балльной шкале оценки по информатике трех учеников. Напишите программу, которая выводит множество оценок, которые есть и у первого и у второго учеников, но которых нет у третьего ученика.

def solution(s1: str, s2: str, s3: str) -> None:
    set1 = set(s1.split())
    set2 = set(s2.split())
    set3 = set(s3.split())
    set12 = set1 & set2
    set123 = set12 - set3
    result = [int(digit) for digit in set123]
    result.sort(reverse=True)
    print(*result)
    return


solution(input(), input(), input())
