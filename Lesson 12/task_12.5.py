# IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.
#
# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.


from random import randint


def generate_ip() -> str:
    result = ''
    for _ in range(4):
        result += f'{randint(0, 255)}.'
    return result.strip('.')
