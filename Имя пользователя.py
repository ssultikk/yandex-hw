chars = ['_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

word = list(input("Введите строку: "))

for i in word:
    # Проверяем, что символ - маленькая латинская буква или входит в список chars
    if ('a' <= i <= 'z') or i in chars:
        pass
    else:
        print('Неверный символ:', i)
        break
else:
    print('OK')
