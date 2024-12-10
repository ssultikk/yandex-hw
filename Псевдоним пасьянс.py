all_rock = int(input())
prev = 1
while prev != 0:
    step = int(input())
    if step <= 3 and step <= all_rock:
        prev = all_rock - step
        print(prev)
        all_rock = prev
    else:
        print(all_rock)
