from collections import Counter

DETAILS_PER_SLON = {'хобот': 1, 'хвост': 1, 'рот': 1, 'ухо': 2, 'глаз': 2, 'нога': 4}
cc = Counter()

while True:
    try:
        n = int(input())
    except ValueError:
        continue

    s = input().strip()
    if s == 'ОБЕД':
        print('Какие-то слоны нецелые. Пошли обедать.')
        break
    if s in DETAILS_PER_SLON:
        cc[s] += n / DETAILS_PER_SLON[s]
        if len(cc) == len(DETAILS_PER_SLON):
            res = int(min(cc.values()))
            if res > 0:
                print('Есть слон!')
                print(res)
                break

