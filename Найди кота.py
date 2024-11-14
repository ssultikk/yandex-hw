n = int(input())
numbers = []

for i in range(n):
    number = input()
    numbers.append(number)

found = False
for number in numbers:
    if ("Кот" in number or "кот" in number):
        found = True
        break

if found:
    print("МЯУ")
else:
    print("НЕТ")
