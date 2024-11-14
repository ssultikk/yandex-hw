foundline = -1
linenum = 0
countcats = 0
while True:
    line = input()
    linenum += 1
    if line == "СТОП":
        break

    if ("Кот" in line or "кот" in line):
        if foundline == -1:
            foundline = linenum
        countcats += 1
print(countcats, foundline)