n = int(input())
keys = []
words = []
for _ in range(n):
    keys.append(input())

num = int(input())
for _ in range(num):
    words.append(input())

for i in words:
    if i in keys:
        print(i)