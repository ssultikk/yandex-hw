n = int(input())
kortez = []
for _ in range(n):
    name = input()
    kortez.append(name)
    print(name)
print()

for i in range(len(kortez)):
    if "5" in kortez[i] or "4" in kortez[i]:
        print(kortez[i])
