city1 = input()
city2 = input()
while city1[-1] == city2[0]:
    city1 = city2
    city2 = input()
print(city2)