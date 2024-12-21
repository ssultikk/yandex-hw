n = int(input())
average = 0

for i in range(n):
    iq = int(input())
    average += iq
    current_average = average / (i + 1)

    if iq > current_average:
        print('>')
    elif iq == current_average:
        print('0')
    else:
        print('<')
