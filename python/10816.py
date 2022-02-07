n = int(input())

cards = list(map(int, input().split()))
card_index = {}
for i in cards:
    if i in card_index:
        card_index[i] += 1
    else:
        card_index[i] = 1
m = int(input())

test = list(map(int, input().split()))

for i in test:
    if i in card_index:
        print(card_index[i], end=' ')
    else:
        print(0, end=' ')
