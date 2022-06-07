# На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит все числа в порядке возрастания, которые есть как в первой строке, так и во второй.

def solution(s1: str, s2: str) -> None:
    set1 = set([int(num) for num in s1.split()])
    set2 = set([int(num) for num in s2.split()])
    set3 = set1 & set2
    result = list(set3)
    result.sort()
    print(*result)
    return


s1, s2 = input(), input()
solution(s1, s2)
