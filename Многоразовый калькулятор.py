second_num = True

while True:
    san = 0
    san2 = 0

    san = int(input())
    simvol = input()

    if simvol in ["+", "-", "*", "/"]:
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

    elif simvol == "!":
        if san > 1:
            factorial = 1
            temp_san = san
            while temp_san > 1:
                factorial *= temp_san
                temp_san -= 1
            print(factorial)
            second_num = False

    elif simvol == "x":
        second_num = False
        print(san)