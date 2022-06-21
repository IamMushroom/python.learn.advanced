# Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур, однако к концу игры ввиду своего возраста забывают, какие города уже называли.
#
# Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.

def solution(__city: str, __cities: set[str]) -> str:
    if __city in __cities:
        result = 'REPEAT'
    else:
        result = 'OK'
    return result


n = int(input())
cities = {input().lower() for _ in range(n)}
print(solution(input().lower(), cities))
