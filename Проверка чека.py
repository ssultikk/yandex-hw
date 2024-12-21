a = input()
n, total = int(a[:4]), int(a[4:])
errors, true_total = [], 0 

for i in range(n):
    a = input()
    price, amount, cost = int(a[:7]), int(a[8:12]), int(a[13:])

    if price * amount != cost:
        errors.append(i + 1)
    true_total += price * amount

print(total - true_total)
for j in errors:
    print(j, end=' ')