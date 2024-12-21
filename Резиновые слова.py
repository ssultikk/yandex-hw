word = input()
n = len(word)
space = (n - 1) // 2

center = ' ' * space + word[space:space + (n - 1) % 2 + 1]
print(center)

for i in range(1, space + 1):
    left_spaces = ' ' * (space - i)
    middle_spaces = ' ' * (2 * i - n % 2)
    
    line = left_spaces + word[space - i] + middle_spaces + word[space + i + (n - 1) % 2]
    
    print(line)
