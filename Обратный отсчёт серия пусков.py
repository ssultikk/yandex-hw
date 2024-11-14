n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print(f"Осталось секунд: {i - j - 1}")
    print(f"Пуск {i}")