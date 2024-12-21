spisk = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
n = int(input())
count = 0

while n != 0:
    print(spisk[count])
    count += 1
    n -= 1
    if count == 5:
        count = 0
