n = int(input())
san = []
for i in range(n):
    san.append(input())
for i in range(n):
    for j in range(i + 1, n):
        if san[i] > san[j]:
            san[i], san[j] = san[j], san[i]
for i in range(n):
    print(san[i])