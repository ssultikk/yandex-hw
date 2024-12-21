A, B, C = ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']
A[0], A[1], A[2], A[3], A[4] = [' *   '], ['* *  '], ['***  '], ['* *  '], ['* *  ']
B[0], B[1], B[2], B[3], B[4] = ['**   '], ['* *  '], ['**   '], ['* *  '], ['**   ']
C[0], C[1], C[2], C[3], C[4] = [' *   '], ['* *  '], ['*    '], ['* *  '], [' *   ']
text = input()
x = 0
for i in range(5):
    for y in range(len(text)):
        if text[y] == 'A':
            print(*A[x], end='')
        elif text[y] == 'B':
            print(*B[x], end='')
        elif text[y] == 'C':
            print(*C[x], end='')
    print()
    x += 1