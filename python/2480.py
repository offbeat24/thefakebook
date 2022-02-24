dice = list(map(int, input().split()))

dice_set = set(dice)

score = 0
if len(dice_set) == 3:
    score += max(dice) * 100
elif len(dice_set) == 2:
    score += 1000
    for i in dice:
        if dice.count(i) == 2:
            score += i * 100
            break
else:
    score += 10000 + dice[0]*1000

print(score)
