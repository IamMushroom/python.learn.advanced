num = input()
rank = 3
result = ''

if len(num) <= rank:
    result = num
else:
    for i in range(len(num) // rank):
        for j in range(rank):
            pos = len(num) - j - rank * i
            result = num[pos - 1] + result
        result = ',' + result
    for i in range(len(num) % rank, 0, -1):
        result = num[i - 1] + result
    result = result.lstrip(',')

print(result)
