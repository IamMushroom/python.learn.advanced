# Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет.
# Напишите программу, которая для одного данного слова определяет его синоним.

def make_dict(__num: int) -> dict[str, str]:
    d = {}
    for _ in range(__num):
        key, value = input().split()
        d.update({key: value, value: key})
    return d


def solution() -> None:
    d = make_dict(int(input()))
    print(d[input()])

solution()
