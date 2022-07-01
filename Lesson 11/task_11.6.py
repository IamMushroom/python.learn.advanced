# Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного знака и идет до конца адреса. Например:
# 
# https://beegeek.ru?name=timur     # строка запроса: name=timur
# Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:
# 
# https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green 
# Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса, сформированную из этих параметров.

def build_query_string(__parameters: dict) -> str:
    site_URL = ''
    param_list = []
    for key in __parameters:
        param_list.append(f'{key}={__parameters[key]}&')
    for param in sorted(param_list):
        site_URL += param
    site_URL = site_URL.strip('&')
    return site_URL

param = {'name': 'timur', 'age': 28}
print(build_query_string(param))
