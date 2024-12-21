n = int(input())
waves = []

# Считываем входные данные
for i in range(n):
    line = input()
    *wave_desc, score = line.rsplit(' ', 1)
    wave_desc = ' '.join(wave_desc)
    score = int(score)
    waves.append((i + 1, wave_desc, score))

# Находим и выводим волны, у которых балл меньше следующей
for i in range(n - 1):
    if waves[i][2] < waves[i + 1][2]:
        print((waves[i][0], waves[i][1]))
