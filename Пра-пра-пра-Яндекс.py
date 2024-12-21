spisk = []
n = int(input())

for _ in range(n):
    search = input()
    spisk.append(search)

key = input()

for i in range(len(spisk)):
    if key in spisk[i]:
        print(spisk[i])
