comands = []
score = []
winners = []
losers = []
for _ in range(int(input())):
    comands.append(input())
    score.append(int(input()))

for i in range(len(comands)):
    for j in range(i + 1, len(comands)):
        if score[i] < score[j]:
            comands[i], comands[j] = comands[j], comands[i]
            score[i], score[j] = score[j], score[i]

if len(comands) % 2 != 0:
    winners = comands[0:(len(comands) // 2) + 1]
    losers = comands[(len(comands) // 2) + 1:len(comands)]
else:
    winners = comands[0:len(comands) // 2]
    losers = comands[(len(comands) // 2):len(comands)]

for i in range(len(winners)):
    for j in range(i + 1, len(winners)):
        if winners[i] > winners[j]:
            winners[i], winners[j] = winners[j], winners[i]

for i in range(len(losers)):
    for j in range(i + 1, len(losers)):
        if losers[i] > losers[j]:
            losers[i], losers[j] = losers[j], losers[i]

for item in winners:
    print(item)
for items in losers:
    print(items)
