all_rock = int(input())
prev = 1
while prev != 0:
    step = int(input())
    prev = all_rock - step
    print(prev)
    all_rock = prev
