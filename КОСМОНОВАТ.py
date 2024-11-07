count = 0
maxrost = None
minrost = None

rost = input()

while rost != "!":
    rost = int(rost)
    if 150 < rost < 190:
        count += 1

if maxrost is None or rost > maxrost:
    maxrost = rost
if minrost is None or rost < minrost:
    minrost = rost

rost = input()

    
print(count)
print(minrost, maxrost)