# На вход программе подается строка текста, 
# содержащая символы. Из данной строки формируется список. 
# Напишите программу, которая выводит список, 
# содержащий все возможные подсписки списка, 
# включая пустой список.

st = input().split()

result_list = []
for i in range (len(st) - 1):
    
        