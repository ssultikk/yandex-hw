dangerous_san = False

while True:
    san = int(input())
    if san == 0:
        break

    if (san % 3 == 0) and (san % 7 == 0):
        print("Караул!")
        dangerous_san = True
        break
    elif san % 3 == 0:
        print("несчастливое")
    elif san % 7 == 0:
        print("опасное")
    else:
        print(san)
