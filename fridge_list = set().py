fridge_list = set()
ingredient_eat = set()
n = int(input())

for i in range(n):
    fridge_list.add(input())
recepts = int(input())

for i in range(recepts):
    name_recept = input()
    ingredient_eat_M = int(input())
    flag = True

    for j in range(ingredient_eat_M):
        ingredient_eat.add(input())

    for i in ingredient_eat:
        if not i in fridge_list:
            flag = False
            
    if flag:
        print(name_recept)
    ingredient_eat = set()