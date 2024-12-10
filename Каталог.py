n = int(input())
brands = set()

for _ in range(n):
    brand = input()

    if brand not in brands:
        brands.add(brand)
        print("НЕТ")
    else:
        print("ДА")
