# На вход программе подаются два числа. Напишите программу, которая определяет, входят ли в запись первого числа все цифры, содержащиеся в записи второго (независимо от повтора, то есть количества цифр) числа или нет.

def solution(s1: str, s2: str) -> None:
    set1 = set(s1)
    set2 = set(s2)
    if set1.issuperset(set2):
        print('YES')
    else:
        print('NO')
    return


solution(input(), input())
