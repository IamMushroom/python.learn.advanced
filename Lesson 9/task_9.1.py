# Учитель проверяет домашнее задание в классе и получил следующие ответы: из n школьников у m домашнее задание съела собака, у k отключили свет, а p учеников постигли оба несчастья. Напишите программу, которая определяет сколько человек выполнило домашнее задание.

def solution(__all: int, __light: int, __dog: int, __both: int) -> int:
    result = __all - __light - __dog + __both
    return result


n, m, k, p = int(input()), int(input()), int(input()), int(input())
print(solution(n, m, k, p))
