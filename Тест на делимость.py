numbers = [int(input()) for _ in range(17)]

for i in range(17):
    d = numbers[i]
    if i % d == 0:
        print("ДА")
    else:
        print("НЕТ")
