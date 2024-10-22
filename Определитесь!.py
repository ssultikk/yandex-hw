name = input()
name2 = input()

if name == name2 and (name == "Быть" or "Не быть"):
    print("Выбор сделан!")
elif (name == "Быть" and name2 == "Не быть") or (name == "Не быть" and name2 == "Быть"):
    print("Вот в чём вопрос!")
else:
    print("Определитесь!")