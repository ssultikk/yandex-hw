total = 0

while True:
    price = float(input())
    if price < 0:
        break

    if price > 1000:
        price *= 0.95

    total += price
print(total)