limit = int(input())
a = [1, 1, 1]
for _ in range(limit - 3):
    a.append(sum(a[-3:]))

if limit == 1:
    print(1)
elif limit == 2:
    print("1 1")
else:
    print(*a)