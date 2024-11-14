n = int(input())

found = False
for i in range(n):
    line = input()
    if "Кот" in line or "кот" in line:
        found = True
        break

if found:
    print("МЯУ")
else:
    print("НЕТ")