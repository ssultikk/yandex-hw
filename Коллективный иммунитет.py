yes = 0
total = 0

while True:
    s = input()
    if s == "":
        break
    total += 1
    if s.lower() == "да":
        yes += 1

if total > 0 and yes / total >= 0.8:
    print("Достигли")
else:
    print("Пока нет")
