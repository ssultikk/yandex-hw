all_rock = int(input())
ai_active = -1

while all_rock != 0:
    if ai_active == -1:
        step = all_rock % 4

        if step == 0:
            step = 2
        if step == 1:
            print('1', end=' ')
        else:
            print(step, end=' ')

    elif ai_active == 1:
        step = int(input())

        while not (1 <= step <= 3 and step <= all_rock):
            if step < 1 or step < 3:
                print('Некорректный ход:', step)
            else:
                print('Некорректный ход:', step)

            step = int(input())

        print(step, end=' ')

    all_rock -= step
    ai_active = -ai_active
    print(all_rock)
    
if ai_active == 1:
    print('ИИ выиграл!')
else:
    print('Вы выиграли!')