string = input()

if string.isspace():
    count = 0
else:
    count = 1
    for i in range(len(string) - 1):
        if string[i].isspace() and not string[i + 1].isspace():
            count += 1

print(count)
