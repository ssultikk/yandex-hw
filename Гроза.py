n = int(input())
h = []
aurum = []
for _ in range(n):
    h.append(int(input()))
    aurum.append(float(input()))

for i in range(n - 1):
    for j in range(i + 1, n):
        if h[i] < h[j]:
            h[i], h[j] = h[j], h[i]
            aurum[i], aurum[j] = aurum[j], aurum[i]
        
        if h[i] == h[j] and aurum[i] < aurum[j]:
            aurum[i], aurum[j] = aurum[j], aurum[i]

for i in range(n):
    print(f"({h[i]}, {aurum[i]})")