dari = set()

n = int(input())
for i in range(n):
    number_of_medications = int(input())
    for _ in range(number_of_medications):
        dari.add(input())

print(*dari, sep='\n')
