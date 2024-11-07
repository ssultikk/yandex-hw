n = int(input())

if n >= 0 :
    for i in range(n, -1, -1):
        print("Осталось секунд: " + str(n))
        n -= 1
    print("Пуск!")
else:
    print("Пуск!")