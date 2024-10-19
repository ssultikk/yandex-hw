grad = input()
weather = input()
osadki = input()

if osadki == "нет":
    print(f"Сегодня {grad} градусов Цельсия, {weather}, солнечно.")
elif osadki == "да":
    print(f"Сегодня {grad} градусов Цельсия, {weather}, осадки в виде дождя или снега.")