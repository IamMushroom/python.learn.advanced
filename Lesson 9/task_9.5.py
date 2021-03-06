# Как известно, математики странные люди. Не составляет исключения и Тимур — автор данного курса.
# Каждый день Тимур решает ровно две сложные математические задачи.
# Решая первую задачу, он записывает на первом листочке все числа, которые в ней встречаются.
# Далее он делает паузу и берется за вторую задачу. Затем записывает на втором листочке все числа, которые в ней встречаются.
# После этого он берет еще один листок и выписывает на него все совпадающие числа из первых двух листочков.
# Если такие числа есть, день удался, если общих чисел нет, Тимур считает день неудачным.
#
# Напишите программу, которая находит общие числа двух листочков или сообщает, что день не удался 😏

def solution(__first_task: set[int], __second_task: set[int]) -> set[int]:
    return (__first_task & __second_task)


first_task = {int(num) for num in input().split()}
second_task = {int(num) for num in input().split()}

digits = solution(first_task, second_task)
if len(digits) == 0:
    print('BAD DAY')
else:
    print(*sorted(digits, reverse=True))
