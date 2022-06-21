# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета.
# У руководителя школы есть списки изучающих каждый предмет.
#
# Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.

def solution(__math: set[str], __it: set[str]) -> int:
    return len(__math.symmetric_difference(__it))


n, m = int(input()), int(input())
math = {input() for _ in range(n)}
it = {input() for _ in range(m)}

count = solution(math, it)
if count == 0:
    print('NO')
else:
    print(count)
