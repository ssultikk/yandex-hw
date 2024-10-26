count = 0
maxrost = None
minrost = None

rost = input("Введите рост или '!' для выхода: ")

while rost != "!":
    rost = int(rost)  # Преобразуем в число
    if 150 < rost < 190:
        count += 1

    # Обновляем максимальный и минимальный рост
    if maxrost is None or rost > maxrost:
        maxrost = rost
    if minrost is None or rost < minrost:
        minrost = rost

    # Считываем следующее значение
    rost = input("Введите рост или '!' для выхода: ")

print("Количество людей с ростом между 150 и 190 см:", count)
print("Минимальный рост:", minrost)
print("Максимальный рост:", maxrost)
