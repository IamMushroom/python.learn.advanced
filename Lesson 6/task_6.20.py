# Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Трибоначчи.

def trib(n):
    if n <= 3:
        return (1, ) * n
    else:
        trib_tuple = (1, 1, 1)
        trib_list = list(trib_tuple)
        for i in range(n - 3):
            first_index = len(trib_list) - 3
            next_elem = sum(trib_list[first_index:first_index + 3])
            trib_list.append(next_elem)
        trib_tuple = tuple(trib_list)
        return trib_tuple

n = int(input())
seq = trib(n)

for elem in seq:
    print(elem, end=' ')
