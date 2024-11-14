n = int(input())
groups = [None] * n

for i in range(n):
    tunnels = int(input())
    current_group = [0] * tunnels
    
    for j in range(tunnels):
        current_group[j] = int(input())

    groups[i] = current_group

min_heights = [0] * n

for i in range(n):
    group = groups[i]
    min_height = group[0]
    for height in group:
        if height < min_height:
            min_height = height
    min_heights[i] = min_height

max_min_height = min_heights[0]
road_number = 1

for i in range(1, n):
    if min_heights[i] > max_min_height:
        max_min_height = min_heights[i]
        road_number = i + 1

print(road_number, max_min_height)
