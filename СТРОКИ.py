strok = 0
word = input()

while word != "Спасибо.":
    strok += 1
    word = input()

if word == "Спасибо.":
    strok += 1

print(strok)
