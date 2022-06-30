# Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово (или словосочетание).
# Например, английские слова evil и live – это анаграммы.
#
# На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.

def str_to_dict(__word: str) -> dict[str, int]:
    d = {}
    for char in __word:
        d[char] = d.get(char, 0) + 1
    return d


def solution(__word1: str, __word2: str) -> str:
    if str_to_dict(__word1) == str_to_dict(__word2):
        return 'YES'
    else:
        return 'NO'


print(solution(input(), input()))
