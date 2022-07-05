# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 0 до 99 (включительно).
#
# Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный почтовый индекс Латверии.

from random import choice, randint
from string import ascii_uppercase


def generate_index() -> str:
    return f'{choice(ascii_uppercase)}{choice(ascii_uppercase)}{randint(0, 99)}_{randint(0, 99)}{choice(ascii_uppercase)}{choice(ascii_uppercase)}'
