# Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык.
# Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу.
# Напишите программу создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из этого словаря.

def solution() -> None:
    d = {}
    for _ in range(int(input())):
        string = input()
        key = string.split(':')[0].lower()
        value = string.split(':')[1].strip()
        d.update({key: value})

    words = []
    for _ in range(int(input())):
        words.append(input().lower())

    for word in words:
        print(d.get(word, 'Не найдено'))


solution()
