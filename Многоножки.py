sorok = set()
even = set()
three = set()

n = int(input())

for _ in range(n):
    num = int(input())

    if num > 40:
        sorok.add(num)

    if num % 2 == 0:
        even.add(num)

    if num % 3 == 0:
        three.add(num)

intersection = (
    (sorok & even - three) |
    (sorok & three - even) |
    (even & three - sorok)
)

print(*intersection)