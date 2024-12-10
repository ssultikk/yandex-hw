n = int(input())
list = set()

for _ in range(n):
    city = input()
    list.add(city)

last_city = input()
if last_city in list:
    print("TRY ANOTHER")

else:
    print("OK")