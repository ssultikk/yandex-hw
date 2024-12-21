word = input()

no_space = ''
for i in word:
    if i != ' ':
        no_space += i

n = len(no_space)
is_palindrome = True

for i in range(n // 2):
    if no_space[i] != no_space[n - i - 1]:
        is_palindrome = False
        break

print(is_palindrome)
