# Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов,
# состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
#
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (большая и маленькая буквы);
# «0» (цифра).

from random import choice, randint


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
