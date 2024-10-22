city1 = input()
city2 = input()

if (city1 == "Тула" or city1 == "Пенза") and (city2 == "Пенза" or city2 == "Тула"):
    print("НЕТ")
elif (city1 == "Тула") or (city2 == "Пенза"):
    print("ДА")
else:
    print("НЕТ")