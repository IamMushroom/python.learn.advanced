# Напишите функцию sq_sum(), которая принимает произвольное количество числовых аргументов и возвращает сумму их квадратов.

def sq_sum(*args) -> float:
    sum = 0
    for arg in args:
        sum += (arg * arg)
    return sum


def solution() -> None:
    print(sq_sum(1.5, 2.5))


if __name__ == "__main__":
    solution()
