while True:
    try:
        san = int(input())
        simvol = input().strip()

        if simvol in ["+", "-", "*", "/", "%"]:
            san2 = int(input())
            if simvol == "+":
                print(san + san2)
            elif simvol == "-":
                print(san - san2)
            elif simvol == "*":
                print(san * san2)
            elif simvol == "/":
                if san2 != 0:
                    print(san // san2)
            elif simvol == "%":
                if san2 != 0:
                    print(san % san2)
        elif simvol == "!":
            if san >= 0:
                factorial = 1
                for i in range(2, san + 1):
                    factorial *= i
                print(factorial)
        elif simvol == "x":
            print(san)
            break
        else:
            continue
    except ValueError:
        continue
    except Exception:
        continue
