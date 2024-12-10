list1 = set()
list2 = set()
num = input()

while num != '':
    list1.add(num)
    num = input()
list1.add(num)
num2 = input()

while num2 != '':
    list2.add(num2)
    num2 = input()
intersection = list1 & list2

if not intersection:
    print('EMPTY')
else:
    for i in intersection:
        print(i)