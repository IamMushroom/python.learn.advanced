# На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая определяет количество чисел, которые есть как в первой строке, так и во второй.

def solution(s1: str, s2: str) -> int:
    set1 = set([int(num) for num in s1.split()])
    set2 = set([int(num) for num in s2.split()])
    set3 = set1 & set2
    return len(set3)


s1, s2 = input(), input()
print(solution(s1, s2))
