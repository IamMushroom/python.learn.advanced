# На вход программе подается строка текста.
# Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

import re

def normalize_text(__text: str) -> str:
    __text = __text.lower()
    __text = re.sub(r'[.,;:-?-!]', '', __text)

    return __text


def solution(__text: str) -> str:
    __text = normalize_text(__text)
    d = {}
    words = __text.split()
    for word in words:
        d.setdefault(words.count(word), set()).add(word)

    return (sorted(d[min(d)])[0])


print(solution(input()))
