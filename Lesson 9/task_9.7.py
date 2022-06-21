# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба эти предмета.
# У руководителя школы есть списки изучающих каждый предмет.
#
# Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только математику.

def solution(__math: set[str], __it: set[str]) -> int:
    return len(__math.difference(__it))


n, m = int(input()), int(input())
math = {input() for _ in range(n)}
it = {input() for _ in range(m)}

print(solution(math, it))
