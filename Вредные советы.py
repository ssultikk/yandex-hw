n = int(input())

for _ in range(n):
    word = input()

    if 'Не' in word[0:3] or 'не' in word[0:3]:
        word = word[3:]
    print(word)