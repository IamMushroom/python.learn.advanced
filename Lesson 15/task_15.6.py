# Напишите функцию print_products(), которая принимает произвольное количество аргументов и выводит список продуктов (любая непустая строка) по образцу:
# <номер продукта>) <название продукта> (нумерация продуктов начинается с единицы).
# Если среди переданных аргументов нет ни одного продукта, необходимо вывести текст Нет продуктов.

def print_products(*args) -> None:
    products: list = []
    for arg in args:
        if isinstance(arg, str) and len(arg) > 0:
            products.append(arg)
    if len(products) == 0:
        print("Нет продуктов")
    else:
        for i in range(len(products)):
            print(f"{i + 1}) {products[i]}")


def solution() -> None:
    print_products('Бананы', [1, 2], ('Stepik',),
                   'Яблоки', '', 'Макароны', 5, True)
    print_products([4], {}, 1, 2, {'Beegeek'}, '')


if __name__ == "__main__":
    solution()
