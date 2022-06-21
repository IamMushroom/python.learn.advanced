# Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета.
# У руководителя школы есть списки учеников, изучающих каждый предмет. Случайно списки всех учеников перемешались.
#
# Напишите программу, которая позволит руководителю выяснить, сколько учеников изучает только один предмет.

def only_one(__students: list[str]) -> int:
    return (len(__students) - len(set(__students))) * 2


n, m = int(input()), int(input())
students = [input() for _ in range(n + m)]

count = n + m - only_one(students)
if count == 0:
    print('NO')
else:
    print(count)
