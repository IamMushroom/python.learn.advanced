# Напишите программу для определения общего количества различных слов в строке текста.

def normalize_text(s: str) -> str:
    chars = ('.,;:-?!')
    for char in chars:
        s = s.replace(char, '')
    return s


text = input().lower()
words = set([normalize_text(word) for word in text.split()])
print(*words)
print(len(words))
