all_n = int(input())
words = []
for _ in range(all_n):
    words.append(input())

n = int(input())
for _ in range(n):
    swipe = int(input())

    new_place = []
    for _ in range(swipe):
        new_place.append(int(input()) - 1)

    new_cups = []
    for i in new_place:
        new_cups.append(words[i])
    
    words = new_cups


for item in words:
    print(item)
