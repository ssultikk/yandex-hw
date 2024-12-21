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

for item in spisk:
    if all(key in item for key in keys):
        print(item)
