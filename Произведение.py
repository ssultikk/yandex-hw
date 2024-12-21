n = int(input())
san = []
for _ in range(n):
    san.append(int(input()))
key = int(input())

found = False
for i in range(n):
    for j in range(i + 1, n):
        if san[i] * san[j] == key:
            print("ДА")
            found = True
            break
    if found:
        break

if not found:
    print("НЕТ")
