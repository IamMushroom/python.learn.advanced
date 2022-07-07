# На вход программе подается натуральное число n.
# Напишите программу, которая выводит в порядке возрастания все несократимые дроби, заключённые между 0 и 1, знаменатель которых не превосходит nn.

from fractions import Fraction
from math import gcd


def solution() -> None:
    n = int(input())
    fraction_list: list[Fraction] = []
    for i in range(1, n):
        for j in range(n, i, -1):
            num = Fraction(i, j)
            if gcd(j, i) == 1:
                fraction_list.append(num)
    
    for num in sorted(fraction_list):
        print(num)


if __name__ == '__main__':
    solution()
