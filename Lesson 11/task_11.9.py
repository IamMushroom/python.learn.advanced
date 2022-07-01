# Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем интернет-магазина.


def make_shopping_dict(__count: int) -> dict[str, dict[str, int]]:
    d: dict[str, dict[str, int]] = {}
    for _ in range(__count):
        name, grossery, count = input().split()
        d.setdefault(name, dict()).update(
            {grossery: d[name].get(grossery, 0) + int(count)})
    return d


def print_shopping_dict(__shopping_dict: dict[str, dict[str, int]]) -> None:
    for name in sorted(__shopping_dict):
        print(f'{name}:')
        for grossery in sorted(__shopping_dict[name]):
            print(f'{grossery} {__shopping_dict[name][grossery]}')


def solution() -> None:
    shopping_dict = make_shopping_dict(int(input()))
    print_shopping_dict(shopping_dict)


solution()
