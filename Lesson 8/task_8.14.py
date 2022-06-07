# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.

all_words = ''
for _ in range(int(input())):
    all_words += input().lower()

print(len(set(all_words)))
