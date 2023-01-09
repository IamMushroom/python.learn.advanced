# Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера.

def matrix(x=1, y=0, value=0) -> list:
    result = []
    if not y:
        y = x
    for i in range(x):
        row = []
        for j in range(y):
            row.append(value)
        result.append(row)
    return result
