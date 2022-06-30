# Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова
#

digits = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}


def solution(__num: int) -> None:
    result = []
    for digit in str(__num):
        result.append(digits[int(digit)])
    print(*result)


solution(int(input()))
