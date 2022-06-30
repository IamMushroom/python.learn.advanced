# На вход программе подаются два предложения.
# Напишите программу, которая определяет, являются они анаграммами или нет.
# Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.

import re


def normalize_string(__string: str) -> str:
    __string = __string.lower().strip()
    __string = __string.replace(' ', '')
    __string = re.sub(r'[.,;:-?-!]', '', __string)

    return __string


def str_to_dict(__word: str) -> dict[str, int]:
    d = {}
    for char in normalize_string(__word):
        d[char] = d.get(char, 0) + 1
    return d


def solution(__word1: str, __word2: str) -> str:
    if str_to_dict(__word1) == str_to_dict(__word2):
        return 'YES'
    else:
        return 'NO'


print(solution(input(), input()))
