first_char = 'а'
last_char = 'я'
alpha = [chr(i) for i in range(ord(first_char), ord(last_char) + 1)]

string = input() + ' запретил букву'
words = string.split()

for char in alpha:
    if char in string:
        print(*words, char)
        string = string.replace(char, '')
        for i in range(len(words)):
            words[i] = words[i].replace(char, '')
            if words[i] == '':
                del words[i]
                break
