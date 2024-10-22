name = input()
adres = input()
if ("@" in name) and ("@" not in adres):
    print("Некорректный логин")
elif ("@" not in adres) and ("@" in name):
    print("Некорректный адрес")
else:
    print("OK")