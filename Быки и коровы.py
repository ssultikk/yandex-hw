byk = 0
cow = 0

word1 = input()
word2 = input()

for i in range(0, len(word1)):
    if word1[i] == word2[i]:
        byk += 1
        
    else:
        for j in range(0, len(word1)):
            if word1[i] == word2[j]:
                cow += 1

    
print(byk, cow)