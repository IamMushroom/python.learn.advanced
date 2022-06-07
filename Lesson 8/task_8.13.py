# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.

words = []
for _ in range(int(input())):
    words.append(set(input().lower()))

for word in words:
    print(len(word))
