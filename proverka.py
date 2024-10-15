user = input("Identify yourself, please!\n")
text = input("Enter the text.\n")
text2 = input("Repeat the text.\n")

if text == text2:
    print(f"{user}, entered correctly!\n")
else:
    print(f"{user}, it didn't work out yet, try again!\n")