# На вход программе подается Decimal число d. Напишите программу, которая вычисляет значение выражения:
# e^{d} + ln(d) + lg (d) + sqrt{d}

from decimal import Decimal


def solution() -> None:
    d = Decimal(input())
    result = d.exp() + d.ln() + d.log10() + d.sqrt()
    print(result)


if __name__ == '__main__':
    solution()
