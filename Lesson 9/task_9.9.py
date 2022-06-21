# Руководитель онлайн-школы BEEGEEK и его помощник составили списки учеников их школы.
#
# Напишите программу, которая выведет все фамилии учеников, которые вспомнили руководитель и его помощник.

def solution(__head: set[str], __assistant: set[str]) -> list[str]:
    return sorted(__head | __assistant)


head = {student for student in input().split()}
assistant = {student for student in input().split()}

print(*solution(head, assistant))
