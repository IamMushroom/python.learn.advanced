# Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.
#
# Например, слова пила и липа или пост и стоп – анаграммы.
#
# Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.

from random import shuffle


def shuffle_word(__word: str) -> str:
    word_list = list(__word)
    shuffle(word_list)
    return ''.join(word_list)


def solution() -> None:
    print(shuffle_word(input()))


if __name__ == '__main__':
    solution()
