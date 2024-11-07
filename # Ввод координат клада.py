# Ввод координат клада
x_treasure = int(input())
y_treasure = int(input())

# Инициализация начальных данных
x, y = 0, 0  # стартовая позиция
direction = 0  # 0 - север, 1 - восток, 2 - юг, 3 - запад
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # (dx, dy) для каждого направления
commands = []
found = False

# Чтение команд
while True:
    try:
        command = input().strip()
        if command == "вперёд":
            steps = int(input().strip())
            commands.append((command, steps))
        else:
            commands.append((command,))
    except EOFError:
        break

# Обработка команд
for i, command in enumerate(commands):
    if command[0] == "вперёд":
        # Движение вперед на заданное число шагов
        steps = command[1]
        x += directions[direction][0] * steps
        y += directions[direction][1] * steps
    elif command[0] == "налево":
        direction = (direction - 1) % 4  # Поворот налево
    elif command[0] == "направо":
        direction = (direction + 1) % 4  # Поворот направо
    elif command[0] == "разворот":
        direction = (direction + 2) % 4  # Разворот

    # Проверка, достигли ли клада
    if (x, y) == (x_treasure, y_treasure):
        found = True
        break

# Вывод результатов
directions_str = ["север", "восток", "юг", "запад"]
print(i + 1)  # Количество команд, выполненных до достижения клада
print(directions_str[direction])  # Текущее направление
