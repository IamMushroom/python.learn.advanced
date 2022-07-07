# Комплексные числа хранятся в списке numbers. Дополните приведенный код так, чтобы он вывел комплексное число с наибольшим модулем и сам модуль числа на отдельных строках.

numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 +
           9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]


def find_max_module(__numbers: list[complex]) -> complex:
    max_abs = float(0)
    max_num = complex(0)
    for num in __numbers:
        if abs(num) > max_abs:
            max_abs = abs(num)
            max_num = num
    return max_num


def solution() -> None:
    max_compl = find_max_module(numbers)
    print(max_compl, abs(max_compl), sep='\n')


if __name__ == '__main__':
    solution()
