san = 0
count = 0
count_active = True

while True:
    n = int(input())

    if n == 0:
        break

    san += n

    if count_active:
        count += 1
    
    if san == 10:
        count_active = False

print(count)