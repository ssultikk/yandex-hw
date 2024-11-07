n = int(input())
numbers = []

for i in range(n):
    number = input()
    numbers.append(number)

for num in numbers:
    if num > num:
        print(">")
    if num < num:
        print("<")
    if num == num:
        print("=")
    
    print(num)