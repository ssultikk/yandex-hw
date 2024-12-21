n = int(input())
san = []

for _ in range(n):
    san.append(int(input()))

p = int(input())
q = int(input())

print(sum(san[p - 1:q]))