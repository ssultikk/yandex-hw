divisors = []

for i in range(1, 10001):
    for j in range(1, int(i**0.5) + 1):
        if i % j == 0:
            divisors += [i]
            if j != i // j:
                divisors += [i // j]


print(divisors)