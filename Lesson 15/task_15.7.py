# Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает именованные аргументы в соответствии с образцом: 
# <имя аргумента>: <значение аргумента>, при этом имена аргументов следуют в алфавитном порядке (по возрастанию).

def info_kwargs(**kwargs) -> None:
    for arg in sorted(kwargs):
        print(f"{arg}: {kwargs[arg]}")

def solution() -> None:
    info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher') 

if __name__ == "__main__":
    solution()