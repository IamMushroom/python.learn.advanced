num = input()
last_digits = 5

if len(num) <= last_digits:
    reversed_num = num[::-1]
else:
    reversed_num = ''
    for i in range(len(num) - last_digits):
        reversed_num += num[i]
    for i in range(len(num) - 1, len(num) - last_digits - 1, -1):
        reversed_num += num[i]
reversed_num = reversed_num.lstrip('0')

print(reversed_num)
