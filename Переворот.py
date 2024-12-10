n = int(input())
result = ''

while n > 0:
    result += str(n % 10)
    n //= 10

print(int(result))
