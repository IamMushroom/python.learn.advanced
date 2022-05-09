def is_infected(string):
    infected_string = 'anton'
    for char in string:
        if char == infected_string[0]:
            infected_string = infected_string[1::]
        if len(infected_string) == 0:
            break
    return len(infected_string) == 0


n = int(input())
fridges = [input() for _ in range(n)]

for i in range(len(fridges)):
    if is_infected(fridges[i]):
        print(i + 1, end=' ')
