word = input()

for i in range(len(word) - 1):
    if not ord(word[i + 1]) > ord(word[i]):
        print(word[i + 1])
        break
else:
    print("(:_0_:)")
