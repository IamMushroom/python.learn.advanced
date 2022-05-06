n = int(input())
first_quarter, second_quarter, third_quarter, fourth_quarter = 0, 0, 0, 0

for _ in range(n):
    coord = [int(i) for i in input().split()]
    if coord[0] > 0 and coord[1] > 0:
        first_quarter += 1
    elif coord[0] < 0 and coord[1] > 0:
        second_quarter += 1
    elif coord[0] < 0 and coord[1] < 0:
        third_quarter += 1
    elif coord[0] > 0 and coord[1] < 0:
        fourth_quarter += 1

print(f'Первая четверть: {first_quarter}')
print(f'Вторая четверть: {second_quarter}')
print(f'Третья четверть: {third_quarter}')
print(f'Четвертая четверть: {fourth_quarter}')
