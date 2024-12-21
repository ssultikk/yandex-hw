n = int(input())
alternating_sum = 0

for i in range(n):
    number = int(input())
    alternating_sum += number * (-1)**i

print(alternating_sum)