word = input()
n = int(input())
favour = input()
if (0 < n <= len(word)) and favour == word[n - 1] and len(favour) == 1:
    print('ДА')
elif (0 < n <= len(word)) and favour != word[n - 1] and len(favour) == 1:
    print('НЕТ')
else:
    print('ОШИБКА')