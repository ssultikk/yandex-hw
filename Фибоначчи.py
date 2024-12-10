limit = int(input())
prev1 = 1
prev2 = 1

while prev1 <= limit:
    print(prev1)
    new = prev1 + prev2
    prev1 = prev2
    prev2 = new