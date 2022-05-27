# Дополните приведенный код так, чтобы переменная new_tuples,
# содержала список кортежей на основе списка tuples с последним элементом каждого кортежа, замененным на численное значение 100.

tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90),
          (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = []
n = 100

for elem in tuples:
    elem = list(elem)
    elem[len(elem) - 1] = n
    new_tuples.append(tuple(elem))

print(new_tuples)
