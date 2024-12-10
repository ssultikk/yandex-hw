eng_n = int(input())
ger_n = int(input())

student_list = set()
languages = set()

for _ in range(eng_n + ger_n):
    students = input()

    if students in languages:
        student_list.add(students)
    else:
        languages.add(students)

difference = languages - student_list

if not difference:
    print('NO')
else:
    print(len(difference))