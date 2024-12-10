n = int(input()) 
a = []
s = "ABCDEFGHI"
 
if n < 10:
    a = [[j+1 for j in range(9)] for i in range(9)]
 
for i in range(n-1, -1, -1):
    for j in range(n):
        print(s[j] + str(a[j][i]), end=' ')
    print()