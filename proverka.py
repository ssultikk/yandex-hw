user = input("Identify yourself, please!")
text = input("Enter the text.")
text2 = input("Repeat the text.")

if text == text2:
    print(f"{user}, entered correctly!")
else:
    print(f"{user}, it didn't work out yet, try again!")