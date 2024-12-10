number_of_dishes = int(input())
dish_list = set()
order_list = set()

for _ in range(number_of_dishes):
    dish_list.add(input())

n = int(input())
for i in range(n):
    number_of_orders = int(input())
    for _ in range(number_of_orders):
        order_list.add(input())

print(*sorted(dish_list - order_list), sep='\n')
