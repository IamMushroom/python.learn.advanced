# Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 1 до 75 (включительно),
# при этом центральная клетка является пустой (она заполняется числом 0).
#
# Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.


from random import randint


def generate_bingo_card() -> list[list[int]]:
    result: list[list[int]] = []
    numbers = set()
    for _ in range(5):
        row: list[int] = []
        while len(row) < 5:
            number = randint(1, 75)
            if number not in numbers:
                numbers.add(number)
                row.append(number)
        result.append(row)
    result[2][2] = 0
    return result


def print_bingo_card(__bingo_card: list[list[int]]) -> None:
    for row in __bingo_card:
        for num in row:
            print(str(num).ljust(3), end='')
        print()


def solution() -> None:
    bingo_card = generate_bingo_card()
    print_bingo_card(bingo_card)


if __name__ == '__main__':
    solution()
