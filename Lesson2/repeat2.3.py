# вводим строку
string = input()

# рассчитываем стоимость
char_cost = 60
c_in_r = 100
cost_c = len(string) * char_cost
cost_r = cost_c // c_in_r
cost_c -= cost_r * c_in_r

# выводим стоимость
print(f'{cost_r} р. {cost_c} коп.')