flips = list(input())

max_count = 0
count = 0
for flip in flips:
    if flip == 'Р':
        count += 1
        if count > max_count:
            max_count = count
    else:
        if count != 0:
            count = 0

print(max_count)
