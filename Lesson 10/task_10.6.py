# На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры.
# Поскольку с каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш.
# При однократном нажатии цифры генерируется первый символ, указанный для этой клавиши.
# Нажатие цифры 2, 3, 4 или 5 раз генерирует второй, третий, четвертый или пятый символ клавиши.

d = {
    "1": [".", ",", "?", "!", ":"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": [" "]
}


def solution(__string: str) -> None:
    result = ''
    for char in __string.upper():
        for key in d:
            if char in d[key]:
                result += key * (d[key].index(char) + 1)
                break
        continue
    print(result)


solution(input())