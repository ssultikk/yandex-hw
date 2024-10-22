apel = int(input())
dol = int(input())

if dol == 0:
    print("Не делится!")
else:
    guys = apel // dol
    osta = dol * guys
    print("Каждому по", guys)
    print("Осталось", apel - osta)