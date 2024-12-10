n = int(input())
names = [input() for _ in range(n)]
answer = 0

for i in set(names):
    count = 0
    for name in names:
        if i == name:
            count += 1

    if count > 1:
        answer += count
print(answer)