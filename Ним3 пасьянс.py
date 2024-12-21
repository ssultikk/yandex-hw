rock1 = int(input())
rock2 = int(input())
rock3 = int(input())

while (rock2 != 0) or (rock1 != 0) or (rock3 != 0):
    which = int(input())
    step = int(input())
    if which == 1:
        rock1 -= step
        print(rock1, rock2, rock3)

    elif which == 2:
        rock2 -= step
        print(rock1, rock2, rock3)

    elif which == 3:
        rock3 -= step
        print(rock1, rock2, rock3)