# На вход программе подается список стран и городов каждой страны.
# Затем даны названия городов.
# Напишите программу, которая для каждого города выводит, в какой стране он находится.

def make_dict(__num: int) -> dict[str, str]:
    d = {}
    for _ in range(__num):
        value, *keys = input().split()
        d.update(dict.fromkeys(keys, value))
    return d


def solution() -> None:
    d = make_dict(int(input()))
    cities = [input() for _ in range(int(input()))]

    for city in cities:
        print(d[city])


solution()
