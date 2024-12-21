n = int(input())
san = []
answer = []
not_answer = []

for _ in range(n):
    san.append(int(input()))

if n % 2 == 0:
    for number in san:
        if number % 2 == 0:
            answer.append(number)
        else:
            not_answer.append(number)

else:
    for number in san:
        if number % 2 != 0:
            answer.append(number)
        else:
            not_answer.append(number)


print(sum(not_answer), answer)
