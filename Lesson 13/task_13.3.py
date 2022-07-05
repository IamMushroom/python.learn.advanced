# Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.

from decimal import Decimal


def get_min_max_digit_sum(__num: str) -> int:
    """
    Возвращает сумму минимальной и максимальной цифры в числе
    """
    num = Decimal(__num)
    if num.as_tuple().exponent + len(num.as_tuple().digits):
        return min(num.as_tuple().digits) + max(num.as_tuple().digits)
    else:
        return max(num.as_tuple().digits)


def solution() -> None:
    """
    Решение
    """
    print(get_min_max_digit_sum(input()))


if __name__ == '__main__':
    solution()
