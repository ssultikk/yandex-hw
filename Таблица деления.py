n = int(input())
m = int(input())

for j in range(1, m + 1):
    print(*(n / j for n in range(1, n + 1)), sep=' ')