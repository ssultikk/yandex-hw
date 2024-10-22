time = input()

if 5 <= time <= 10:
    print("Утро")
elif 11 <= time <= 17:
    print("День")
elif 18 <= time <= 22:
    print("Вечер")
elif 23 <= time <= 24 or 0 <= time <= 4:
    print("Ночь")
else:
    print("Ошибка")