fib1 = 1
fib2 = 1

number = int(input())
position = 2

while fib2 < number:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    position += 1

if fib2 == number:
    print(position)
else:
    print('НЕТ')
