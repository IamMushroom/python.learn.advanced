# Напишите функцию mean(), которая принимает произвольное количество аргументов и возвращает среднее арифметическое переданных в нее числовых (int или float) аргументов.

def mean(*args) -> float:
    avg: float = 0
    count: int = 0
    for arg in args:
        if type(arg) is int or type(arg) is float:
            avg += arg
            count += 1
    result: float = 0
    if count != 0:
        result = avg / count
    return result

def solution() -> None:
    print(mean())
    print(mean(7))
    print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
    print(mean(True, ['stepik'], 'beegeek', (1, 2)))
    print(mean(-1, 2, 3, 10, ('5')))
    print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

if __name__ == "__main__":
    solution()
