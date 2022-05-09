# вводим данные
weight, height = float(input()), float(input())

# расчитываем ИМТ
BMI = weight / height ** 2
if BMI < 18.5:
    result = 'Недостаточная масса'
elif BMI > 25:
    result = 'Избыточная масса'
else:
    result = 'Оптимальная масса'

# выводим интерпретацию
print(result)
