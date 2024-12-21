n = int(input())
count = 0

while True:
    a = input()

    if "КОНЕЦ" == a:
        break

    elif "доска" in a or "дощечка" in a:
        count += 1
        if count == n:
            print(f"Прибили {count} дощечку.")
            break
        print(f"Прибили {count} дощечку.")

if count < n:
    print("МАЛОВАТО")
elif count >= n:
    print("ГОТОВО")


