# Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним решать задачи по программированию.

from random import choice


def get_students(__count: int) -> list[str]:
    """
    Формируется список из __count студентов
    """
    result: list[str] = []
    for _ in range(__count):
        result.append(input())
    return result


def generate_secret_friend(__students: list[str]) -> dict[str, str]:
    """
    Для каждого студента из списка __students подбирается тайный друг из этого же списка
    """
    secret_friends: set[str] = set()
    result: dict[str, str] = dict()
    for student in __students:
        friend = student
        while friend == student or friend in secret_friends:
            friend = choice(__students)
        secret_friends.add(friend)
        result[student] = friend
    return result


def print_friends(__students: dict[str, str]) -> None:
    """
    Выводятся пары студент - тайный друг, каждая на новой строке
    """
    for student in __students:
        print(f'{student} - {__students[student]}')


def solution() -> None:
    """
    Решение задачи
    """
    students = get_students(int(input()))
    secret_friends = generate_secret_friend(students)
    print_friends(secret_friends)


if __name__ == '__main__':
    solution()
