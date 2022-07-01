# В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik, проник опасный вирус и сломал контроль прав доступа к файлам.
# Говорят, вирус написал один из студентов курса Python для начинающих.
#
# Для каждого файла известно, с какими действиями можно к нему обращаться:
#
# запись W (write, доступ на запись в файл);
# чтение R (read, доступ на чтение из файла);
# запуск X (execute, запуск на исполнение файла).
# Напишите программу для восстановления контроля прав доступа к файлам.
# Ваша программа для каждого запроса должна будет возвращать OK если выполняется допустимая операция, и Access denied, если операция недопустима.


def make_files_flags_dict(__count: int) -> dict[str, list[str]]:
    d: dict[str, list[str]] = {}

    for _ in range(__count):
        key, *values = input().split()
        d.update({key: values})

    return d


def solution() -> None:
    flags = {
        'write': 'W',
        'read': 'R',
        'execute': 'X'
    }
    files_flags = make_files_flags_dict(int(input()))
    commands_count = int(input())
    commands_result: list[str] = []

    for _ in range(commands_count):
        command, file = input().split()
        if flags[command] in files_flags[file]:
            commands_result.append('OK')
        else:
            commands_result.append('Access denied')

    print(*commands_result, sep='\n')


solution()
