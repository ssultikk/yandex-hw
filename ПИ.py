n = int(input())

pi_approximation = 0
for k in range(n):
    pi_approximation += ((-1) ** k) / (2 * k + 1)
pi_approximation *= 4

print(pi_approximation)
