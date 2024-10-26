count = 0
san = int(input())

if (san % 2 == 0) and (san != 0):
    while (san != 1):
        count += 1
        san = san // 2
    print(count)
else:
    print("НЕТ")