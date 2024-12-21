numbers = input().split(' ')
print(*["*" * int(n) for n in numbers], sep='\n')
