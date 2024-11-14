price1 = int(input())
price2 = int(input())

active_flag = False

while price2 != 0:
    if not active_flag:
        if price1 < price2:
            growth_price = price2
            active_flag = True

    if active_flag:
        if price1 > price2:
            fall_price = price2
            break

    price1 = price2
    price2 = int(input())

print(growth_price, fall_price, fall_price - growth_price)