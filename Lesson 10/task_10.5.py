# Напишите программу, которая по номеру курса выводит информацию о данном курсе.

agenda = {'CS101': {'class': 3004, 'teacher': 'Хайнс', 'time': '8:00'},
          'CS102': {'class': 4501, 'teacher': 'Альварадо', 'time': '9:00'},
          'CS103': {'class': 6755, 'teacher': 'Рич', 'time': '10:00'},
          'NT110': {'class': 1244, 'teacher': 'Берк', 'time': '11:00'},
          'CM241': {'class': 1411, 'teacher': 'Ли', 'time': '13:00'}}


def solution(__course: str) -> None:
    print(
        f'{__course}: {agenda[__course]["class"]}, {agenda[__course]["teacher"]}, {agenda[__course]["time"]}')


solution(input())
