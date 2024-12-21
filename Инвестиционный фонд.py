spisk = []
n = int(input())
for _ in range(n):
    num = int(input())
    spisk.append(num)
    print(num)
print()
for i in range(len(spisk)):
    print(spisk[i] * 3)