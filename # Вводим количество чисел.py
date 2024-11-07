# Вводим количество чисел
n = int(input("Введите количество чисел: "))

# Инициализируем сумму
alternating_sum = 0

# Обрабатываем вводимые числа и вычисляем чередующуюся сумму
for i in range(n):
    num = int(input(f"Введите число {i + 1}: "))
    # Если индекс чётный, прибавляем, иначе вычитаем
    if i % 2 == 0:
        alternating_sum += num
    else:
        alternating_sum -= num

# Выводим результат
print("Результат:", alternating_sum)

