# Напишите функцию count_args(), которая принимает произвольное количество аргументов и возвращает количество переданных в нее аргументов.

def count_args(*args) -> int:
    return len(args)


def solution() -> None:
    print(count_args('stepik', 'beegeek'))


if __name__ == '__main__':
    solution()
