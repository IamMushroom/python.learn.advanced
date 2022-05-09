n, k = int(input()), int(input())
live_list = [i + 1 for i in range(n)]

i = 0
while len(live_list) > 1:
    pos = (i + k - 1) % len(live_list)
    del live_list[pos]
    i = pos
print(*live_list)
