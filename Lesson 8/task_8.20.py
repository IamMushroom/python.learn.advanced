# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке. Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.

def solution(n: int) -> None:
    numbers = []
    for _ in range(n):
        numbers.append(set(input()))
    same_digits = numbers[0]
    for number in numbers:
        same_digits &= number
    result = [int(digit) for digit in same_digits]
    result.sort()
    print(*result)
    return None


n = int(input())
solution(n)
