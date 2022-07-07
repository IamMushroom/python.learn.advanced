# На вход программе подается натуральное число n.
# Напишите программу, которая находит наибольшую правильную несократимую дробь с суммой числителя и знаменателя равной n


from fractions import Fraction
from math import gcd


def solution() -> None:
    n = int(input())
    max_F = Fraction(0)
    for denomirator in range(n, n // 2, -1):
        numerator = n - denomirator
        num = Fraction(numerator, denomirator)
        if gcd(numerator, denomirator) == 1 and numerator < denomirator:
            max_F = max(num, max_F)
    print(max_F)


if __name__ == '__main__':
    solution()
