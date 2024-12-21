san = []
n = int(input())
for i in range(n):
    san.append(int(input()))
    if i > 0:
        print(san[i - 1] + san[i])