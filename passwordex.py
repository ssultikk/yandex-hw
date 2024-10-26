while True:

    cod1, cod2 = input(), input()

    if len(cod1) < 8:
        print("Короткий!")

    elif "123" in cod1:
        print("Простой!")

    elif cod1 != cod2:
        print("Различаются.")

    else:
        print("OK")
        break
