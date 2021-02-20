import numpy as np

'''Rules of the game: 
You start by paying a dollar to roll 8 dice and add up your score
You then check your score against the Razzle Dazzle table
The goal is to get to 100 points which earns you your prize
Table:
If you roll:
8, 9, 47, 48 -> 100 points
10, 12, 13, 43, 44, 46 -> 50 points
11, 45 -> 30 points
14, 42 -> 20 points
15, 41 -> 15 points
16 -> 10 points
17, 39, 40 -> 5 points
18, 19, 20, 21, 35, 36, 37, 38 -> double the prize you're going for (start at $10)
22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34 -> nothing
29 -> You now have to pay twice as much per roll
'''

hundred = [8, 9, 47, 48]
fifty = [10, 12, 13, 43, 44, 46]
thirty = [11, 45]
twenty = [14, 42]
fifteen = [15, 41]
five = [17, 39, 40]
doublePrize = [18, 19, 20, 21, 35, 36, 37, 38]
nothing = [22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34]

score = 0
roll_history = []
prize = 10
fee = 1
spent = 0

for x in range(100):
    roll = 0
    for i in range(8):
        dice = np.random.randint(1, 7)
        roll += dice

    roll_history.append(roll)
    spent = spent + fee

    if roll in hundred:
        score += 100
    elif roll in fifty:
        score += 50
    elif roll in thirty:
        score += 30
    elif roll in twenty:
        score += 20
    elif roll in fifteen:
        score += 15
    elif roll in five:
        score += 5
    elif roll == 16:
        score += 10
    elif roll in doublePrize:
        prize = prize * 2
    elif roll in nothing:
        continue
    elif roll == 29:
        fee = fee * 2

print('score:' + str(score))
print('prize:' + str(prize))
print('fee:' + str(fee))
print('spent: ' + str(spent))
print('rollHistory:' + str(roll_history))
print('num of rounds:' + str(len(roll_history)))
