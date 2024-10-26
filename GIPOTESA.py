count = 0
num = int(input())

while num != 1:
	count += 1
    
	if num % 2 == 0:
		num //= 2
		
	else:
	    
		num = num*3 + 1
		
print(count)