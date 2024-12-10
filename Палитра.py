set1 = set()
set2 = set()
count = 0
n = int(input())

for _ in range(n):
    number_of_palitras = int(input())
    palitras = set(input() for _ in range(number_of_palitras))
    
    for color in palitras:
        if color in set1:
            set2.add(color)
        else:
            set1.add(color)
    
intersection = set1 & set2
count = len(set2)
print(len(intersection), (len(intersection) * 2) + count)
