# Чтение количества показателей
s = int(input())
s_list1 = []
s_list2 = []

# Инициализация показателей для обоих братьев
for _ in range(s):
    value = int(input())
    s_list1.append(value)
    s_list2.append(value)

# Чтение количества тренировок
n = int(input())

# Обработка каждой тренировки
for _ in range(n):
    bro = int(input())  # Номер брата
    s_work = int(input())  # Индекс показателя
    work = int(input())  # Величина увеличения показателя

    if bro == 1:
        s_list1[s_work] += work
    elif bro == 2:
        s_list2[s_work] += work

# Вывод результатов
print(*s_list1)  # Значения показателей первого брата
print(*s_list2)  # Значения показателей второго брата

# Подсчет количества совпадающих показателей
matches = sum(1 for i in range(s) if s_list1[i] == s_list2[i])
print(matches)
