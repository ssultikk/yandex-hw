num = int(input())

if num == 0:
    print(50)

elif num <= 30:
    print(num + num // 2)

elif 31 <= num <= 70:
    print(num + num // 10)

elif num > 70:
    print(num)