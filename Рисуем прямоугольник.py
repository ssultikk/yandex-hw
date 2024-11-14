y = int(input())
x = int(input())
a = input()
print(a * x)

for i in range(y - 2):
    print(a, ' ' * (x - 2), a, sep='')
print(a * x)