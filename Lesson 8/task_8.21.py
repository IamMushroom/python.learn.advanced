# На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

def solution(s1: str, s2: str) -> None:
    set1 = set(s1)
    set2 = set(s2)
    if set1.isdisjoint(set2):
        print('NO')
    else:
        print('YES')
    return


solution(input(), input())
