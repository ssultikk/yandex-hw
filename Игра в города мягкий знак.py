word = input()
word2 = input()

if word[-1] != "ь":
    if word[-1] == word2[0]:
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")

elif word[-1] == "ь":
    if word[-2] == word2[0]:
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")