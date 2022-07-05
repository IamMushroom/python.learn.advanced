# Decimal числа, разделенные символом пробела, хранятся в строковой переменной s.
# Дополните приведенный код, чтобы он вывел на первой строке сумму всех чисел, а на второй строке 5 самых больших чисел в порядке убывания, разделенных символом пробела.

from decimal import Decimal


s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'


def get_decimal_list(__nums: str) -> list[Decimal]:
    """
    Возвращает отсортированный список decimal чисел
    """
    result = [Decimal(i) for i in __nums.split()]
    result = sorted(result, reverse=True)
    return result


def solution() -> None:
    decimal_list = get_decimal_list(s)
    print(sum(decimal_list))
    for i in range(5):
        print(decimal_list[i], end=' ')


if __name__ == '__main__':
    solution()
