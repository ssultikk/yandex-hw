n = int(input())
san = []
for _ in range(n):
    san.append(input())

for i in range(n):
    for j in range(0, n - i - 1):
        if len(san[j]) > len(san[j + 1]) or (len(san[j]) == len(san[j + 1]) and san[j] > san[j + 1]):
            san[j], san[j + 1] = san[j + 1], san[j]

for item in san:
    print(item)
