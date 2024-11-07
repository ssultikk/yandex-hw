count = 0
san = int(input())

while (san % 2 == 0) and (san != 0) and (san != 1):
    count += 1
    san = san // 2

if san == 1:
    print(count)
else:
    print("НЕТ")
