n = int(input())
for i in range(1, n + 1):
    word = input()
    index = -1

    for j in range(len(word) - 2):
        if (word[j] == 'К' and word[j + 1] == 'о' and word[j + 2] == 'т') or \
           (word[j] == 'к' and word[j + 1] == 'о' and word[j + 2] == 'т'):
            index = j
            break
    
    if index != -1:
        print(i, index + 1)
