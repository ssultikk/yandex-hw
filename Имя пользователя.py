chars = ['_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

word = list(input())

for i in word:
    if ('a' <= i <= 'z') or i in chars:
        pass
    else:
        print('Неверный символ:', i)
        break
else:
    print('OK')
