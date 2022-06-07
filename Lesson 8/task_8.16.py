# На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

def solution(s: str) -> None:
    numbers = set()
    for num in s.split():
        if int(num) in numbers:
            print('YES')
        else:
            print('NO')
            numbers.add(int(num))
    return


s = input()
solution(s)
