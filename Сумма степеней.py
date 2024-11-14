n = int(input())
s = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        exponent = 0
        for j in range(2, i + 1, 2):
            exponent += j
    else:
        exponent = 0
        for j in range(1, i + 1, 2):
            exponent += j
    
    result = 1
    for _ in range(exponent):
        result *= i
    
    s += result

print(s)
