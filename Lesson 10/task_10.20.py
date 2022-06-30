# Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.
#
# У каждого из друзей Тимура может быть один или более телефонных номеров.
# Напишите программу, которая поможет Тимуру находить все номера определённого друга.

def make_dict(__num: int) -> dict[str, str]:
    d = {}
    for _ in range(__num):
        value, key = input().lower().split()
        d[key] = d.get(key, '') + ' ' + value
    return d


def solution() -> None:
    d = make_dict(int(input()))
    names = [input().lower() for _ in range(int(input()))]
    for name in names:
        print((d.get(name, 'абонент не найден')).strip())


solution()
