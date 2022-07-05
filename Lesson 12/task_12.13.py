# Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов,
# состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).
# 
# Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной букве в верхнем и нижнем регистре.

from random import choice, randint, shuffle


symbols = {
    1: 'ABCDEFGHJKLMNPQRSTUVWXYZ',
    2: 'abcdefjhijkmnpqrstuvwxyz',
    3: '23456789'
}


def generate_password(__length: int) -> str:
    """
    Генерирует пароль длинной __length
    """
    result = ''
    for _ in range(__length):
        char = choice(symbols[randint(1, 3)])
        result += char
    result = choice(symbols[1]) + choice(symbols[2]) + choice(symbols[3]) + result
    result = result[:__length + 1]
    result_list = list(result)
    shuffle(result_list)
    result = ''.join(result_list)
    return result


def generate_passwords(__count: int, __length: int) -> set[str]:
    """
    Генерирует __count уникальных паролей длинной __length
    """
    result: set[str] = set()
    while len(result) < __count:
        password = generate_password(__length)
        if password not in result:
            result.add(password)
    return result


def solution() -> None:
    """
    Решение
    """
    print(*generate_passwords(int(input()), int(input())), sep='\n')


if __name__ == '__main__':
    solution()
