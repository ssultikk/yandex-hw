all_candys = int(input())
num_tuys = 1

while True:
    numerator = all_candys - (num_tuys * (num_tuys - 1)) // 2
    if numerator % num_tuys == 0:
        min_candys = numerator // num_tuys
        if min_candys > 0: 
            print(min_candys)
            break
    num_tuys += 1
