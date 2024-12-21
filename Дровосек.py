word = input()
n = int(input())

while len(word) > n:
    print(word[-n:])
    word = word[:-n]
    
    if len(word) > n:
        print(word[:n])
        word = word[n:]

if word:
    print(word)
