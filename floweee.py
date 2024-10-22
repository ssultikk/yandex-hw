flower1 = input()
flower2 = input()
flower3 = input()

bouquet = input()

answer = ""

if flower1 in bouquet:
    answer = (f"В букете есть {flower1}")

if flower2 in bouquet:
    if answer == "":
        answer = (f"В букете есть {flower2}")
    else:
        answer += f", {flower2}"

if flower3 in bouquet:
    if answer == "":
        answer = (f"В букете есть {flower3}")
    else:
        answer += f", {flower3}"

if answer == "":
    print("Таких цветов в букете нет.")
else:
    print(answer + '.')