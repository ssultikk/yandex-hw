cod1 = input()

if len(cod1) < 8:
    print("Короткий!")
else:

    if "123" in cod1:
        print("Простой!")
    else:

        cod2 = input()
    
        if cod1 != cod2:
            print("Различаются.")
        else:
            print("OK")
