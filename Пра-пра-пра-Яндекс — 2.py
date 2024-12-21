spisk = []
keys = []
n = int(input())

for _ in range(n):
    search = input()
    spisk.append(search)

n_key = int(input())
for _ in range(n_key):
    key = input()
    keys.append(key)

for i in range(len(spisk)):
    if keys in spisk[i]:
        print(spisk[i])
