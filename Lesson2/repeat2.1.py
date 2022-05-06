# вводим числа
a, b = int(input()), int(input())

# производим арифметические действия
sum = a + b
dif = a - b
mult = a * b
quo = a / b
div = a // b
mod = a % b
root = ((a ** 10) + (b ** 10)) ** 0.5

# выводим результаты
print(sum, dif, mult, quo, div, mod, root, sep='\n')
