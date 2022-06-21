# Руслан получил в конце учебного года список литературы на лето. Теперь ему надо выяснить, какие книги из этого списка у него есть. У Руслана на компьютере в текстовом файле записаны все книги из его домашней библиотеки в случайном порядке.
#
# Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.

def solution(__has: set[str], __need: list[str]) -> list[str]:
    result = []
    for book in __need:
        if book in __has:
            result.append('YES')
        else:
            result.append('NO')
    return result


m, n = int(input()), int(input())
has = {input() for _ in range(m)}
need = [input() for _ in range(n)]

for book in solution(has, need):
    print(book)
