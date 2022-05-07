figures = ['камень', 'ножницы', 'бумага']
result = ['Тимур', 'Руслан', 'ничья']

def knb(st1, st2):
    if st1 == st2:
        return result[2]
    elif st1 == figures[0]:
        if st2 == figures[1]:
            return result[0]
        else:
            return result[1]
    elif st1 == figures[1]:
        if st2 == figures[2]:
            return result[0]
        else:
            return result[1]
    elif st1 == figures[2]:
        if st2 == figures[0]:
            return result[0]
        else:
            return result[1]

tim_fig = input()
rus_fig = input()

print(knb(tim_fig, rus_fig))