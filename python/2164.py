from collections import deque


n = int(input())

cards = deque(range(1, n+1))

while 1:
    if len(cards) <= 1:
        break

    cards.popleft()
    cards.append(cards[0])
    cards.popleft()

print(cards[0])
