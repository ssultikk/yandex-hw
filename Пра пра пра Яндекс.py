n = int(input())
list = []
poisk = input()
for _ in range(n):
    word = input()
    list.append(word)


for i in list:
    if poisk in i:
        print(i)

