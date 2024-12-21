son = []
maxson = ""
while True:
    word = input()
    son.append(word)
    if word == "":
        break

p = int(input())
q = int(input())

for i in son[p - 1:q]:
    if len(i) > len(maxson):
        maxson = i
print(maxson)