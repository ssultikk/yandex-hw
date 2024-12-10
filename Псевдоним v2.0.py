all_rock = int(input())
ai_active = True

while all_rock > 0:
    if ai_active:
        upper_limit = min(3, all_rock)
        ai_step = (id(object()) % upper_limit) + 1
        
        all_rock -= ai_step
        print(ai_step, all_rock)
        
        if all_rock == 0:
            print("ИИ выиграл!")
            break
        ai_active = False

    step = int(input())
    if 1 <= step <= 3 and step <= all_rock:
        all_rock -= step
        print(step, all_rock)
        
        if all_rock == 0:
            print("Вы выиграли!")
            break
        ai_active = True
    else:
        print(f"Некорректный ход: {step}")
