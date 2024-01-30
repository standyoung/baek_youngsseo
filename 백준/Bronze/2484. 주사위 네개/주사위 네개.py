
n = int(input())
cash = 0

for _ in range(n):
    p = list(map(int, input().split()))
    dice = [0] * 7
    prize = 0

    for i in range(4):
        dice[p[i]] += 1

    if dice.count(4) == 1:
        prize += 50000 + (dice.index(4)*5000)
    elif dice.count(3) == 1:
        prize += 10000 + (dice.index(3)*1000)
    elif dice.count(2) == 2:
        prize += 2000
        for j in range(len(dice)):
            if dice[j] == 2:
                prize += j*500
    elif dice.count(2) == 1:
        prize += 1000+dice.index(2)*100
    elif dice.count(1) == 4:
        maxInx = 0
        for j in range(len(dice)):
            if dice[j] == 1 and maxInx < j:
                maxInx = j
        prize += maxInx*100

    if cash <= prize:
        cash = prize

print(cash)
