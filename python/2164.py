n = int(input())

cards = list(range(1, n))

while 1:
    if len(cards) == 1:
        break

    cards.pop()
    cards.append(cards[0])
    del cards[0]

print(cards[0])
