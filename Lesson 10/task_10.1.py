# Дополните приведенный код так, чтобы он вывел сумму минимального и максимального ключа в словаре my_dict.
#
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee',
           7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}


def solution(__dict: dict) -> float:
    return min(__dict) + max(__dict)


print(solution(my_dict))
