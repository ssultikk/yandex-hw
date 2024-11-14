hobot_count = 0
hvost_count = 0
legs_count = 0
ears_count = 0
eyes_count = 0
mouse_count = 0
correct_flag = False
answer = 0

while True:
    n_input = input()

    is_number = True
    for char in n_input:
        if char not in "0123456789":
            is_number = False
            break
    
    if not is_number or n_input == "":
        continue

    n = int(n_input)
    proverka = input()

    if proverka == "хобот":
        hobot_count += n
    elif proverka == "хвост":
        hvost_count += n
    elif proverka == "нога":
        legs_count += n
    elif proverka == "ухо":
        ears_count += n
    elif proverka == "глаз":
        eyes_count += n
    elif proverka == "рот":
        mouse_count += n

    elif proverka == "ОБЕД":
        break

    if hobot_count <= 1 and hvost_count <= 1 and legs_count <= 4 and ears_count <= 2 and eyes_count <= 2 and mouse_count <= 1:
        correct_flag = True
        answer = 1

if correct_flag:
    answer += answer
    print("Есть слон!")
    print(answer)
