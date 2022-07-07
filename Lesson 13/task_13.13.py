# Даны два комплексных числа. Напишите программу, которая вычисляет и выводит их сумму, разность и произведение.

def complex_operations(_num1: complex, _num2: complex) -> None:
    print(f'{_num1} + {_num2} = {_num1 + _num2}')
    print(f'{_num1} - {_num2} = {_num1 - _num2}')
    print(f'{_num1} * {_num2} = {_num1 * _num2}')


def solution() -> None:
    complex_operations(complex(input()), (complex(input())))


if __name__ == '__main__':
    solution()
