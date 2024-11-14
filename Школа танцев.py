nervy = int(input())
count = 0

while nervy:
    for proverka in ("раз", "два", "три", "четыре"):
        if proverka == input():
            count += 1
        else:
            print(f"Правильных отсчётов было {count}, но теперь вы ошиблись.")
            count = 0
            nervy -= 1
            break

print("На сегодня хватит.")
        
    