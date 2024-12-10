maxn = int(input())
n = int(input())

for _ in range(n):
    word = input()

    if len(word) > maxn:
        print(f"{word[0:maxn - 3]}...")
    else:
        print(word)