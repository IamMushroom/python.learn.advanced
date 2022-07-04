# Напишите программу, которая с помощью модуля random генерирует случайный пароль.
# Программа принимает на вход длину пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z (в нижнем и верхнем регистре).


from random import randint


def generate_password(__len: int) -> None:
    result = ''
    for _ in range(__len):
        if randint(0, 1):
            result += chr(randint(65, 90))
        else:
            result += chr(randint(97, 122))
    print(result)


def solution() -> None:
    generate_password(int(input()))


if __name__ == '__main__':
    solution()
