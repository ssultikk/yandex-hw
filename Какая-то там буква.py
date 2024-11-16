word = input()
n = int(input())

if n < 1 or n > len(word):
    print("ОШИБКА")
else:
    print(word[n - 1])