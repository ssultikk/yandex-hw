eng_n = int(input())
ger_n = int(input())

eng_list = set()
ger_list = set()

for _ in range(eng_n):
    eng_stu = input()
    eng_list.add(eng_stu)

for _ in range(ger_n):
    ger_stu = input()
    ger_list.add(ger_stu)

intersection = eng_list & ger_list

if (eng_n + ger_n) == (len(intersection) * 2):
    print('NO')

else:
    print((eng_n + ger_n) - (len(intersection) * 2))