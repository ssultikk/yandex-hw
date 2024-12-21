stroka = input()
promej = []
eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"'
ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
flag = True
for i in range(len(eng) - 1):
    if eng[i] in stroka:
        flag = False
stroka.split()
for i in stroka:
    for j in i:
        if "!" in j or ',' in j or ',' in j or " " in j or '.' in j or '?' in j or '…' in j or '’' in j:
            continue
        elif j not in promej:
            promej.append(j)
for i in set(promej):
    for j in i:
        if flag:
            print("('" + str(j) + "', " + str(ru.index(j) + 1) + ")")
        else:
            print("('" + str(j) + "', " + str(eng.index(j) + 1) + ")")