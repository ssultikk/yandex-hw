max_word = ""
min_word = ""
count = 0

while True:
    word = input()

    if word == "стоп":
        break

    if max_word == "" or len(word) > len(max_word):
        max_word = word
    
    if min_word == "" or len(word) < len(min_word):
        min_word = word

set_max = set(max_word)
set_min = set(min_word)

if set_min.issubset(set_max):
    print("ДА")
else:
    print("НЕТ")
