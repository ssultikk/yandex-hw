n = int(input())
word = input()

for i in word:
    m = ord(i) + n
    
    if 'А' <= i <= 'Я':
        if m > ord('Я'):
            m -= 32
    elif 'а' <= i <= 'я':
        if m > ord('я'):
            m -= 32
        
    if 1040 <= m <= 1071 or 1072 <= m <= 1103:
        print(chr(m), end='')
    else:
        print(i, end='')
