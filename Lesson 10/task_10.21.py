# Напишите программу для расшифровки секретного слова методом частотного анализа.

def make_dict(__num) -> dict[int, str]:
    d = {}
    for _ in range(__num):
        value, key = input().split(':')
        d.update({int(key): value})
    return d


def solution() -> None:
    word_dict = {}
    word = input()
    for char in word:
        word_dict[char] = word_dict.get(char, 0) + 1
    d = make_dict(int(input()))
    decrypt_word = ''
    for char in word:
        decrypt_word += d[word_dict[char]]
    print(decrypt_word)


solution()
