bad_last_input = False
count_dobri = 0
count_zloi = 0

while True:
    current_input = input()
    if not current_input:
        break

    if current_input == "добрый":
        count_dobri += 1
        bad_last_input = False

    if current_input == "злой":
        count_zloi += 1
        bad_last_input = True
    
    if current_input == "Какой подарок?":
        if (count_dobri > count_zloi) and (not bad_last_input):
            print("серебряный шиллинг")

        elif (count_dobri < count_zloi) and (bad_last_input):
            print("золотой")
        
        else:
            print("Ах, не знаю!")
            break
        count_dobri = 0
        count_zloi = 0


