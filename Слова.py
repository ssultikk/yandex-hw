s = input()

word = ''

for char in s:
    if char != ' ':
        word += char
    else:
        if word:
            print(word)
            word = ''

if word:
    print(word)
