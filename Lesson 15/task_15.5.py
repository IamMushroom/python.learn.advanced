# Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно) и возвращает приветствие в соответствии с образцом.

def greet(first, *args) -> str:
    result = f"Hello, {first}"
    for arg in args:
        result += f" and {arg}"
    result += "!"
    return result

def solution() -> None:
    print(greet('Timur'))
    print(greet('Timur', 'Roman'))
    print(greet('Timur', 'Roman', 'Ruslan'))

if __name__ == "__main__":
    solution()