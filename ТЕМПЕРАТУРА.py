count = 0
average = 0
temp = float(input())

while temp >= -300:
    count += 1
    average += temp
    temp = float(input())

answer = average / count

print(f"{answer:.1f}")
