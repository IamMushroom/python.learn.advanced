# Дано натуральное число n и два комплексных числа z_1, z_2
# Напишите программу, которая вычисляет и выводит значение выражения

def solve_task(_num: int, _compl1: complex, _compl2: complex) -> complex:
    first_elem = _compl1 ** _num
    second_elem = _compl2 ** _num
    third_elem = _compl1.conjugate() ** _num
    fourth_elem = _compl2.conjugate() ** (_num + 1)

    return first_elem + second_elem + third_elem + fourth_elem


def solution() -> None:
    sol = solve_task(int(input()), complex(input()), complex(input()))
    print(sol)


if __name__ == '__main__':
    solution()
