count = 0
found = False
fraza = ""
while fraza != "СТОП":
    fraza = input()
    if ("Кот" in fraza or "кот" in fraza):
        found = True
        break
