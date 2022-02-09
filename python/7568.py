n = int(input())

peep = list()

for i in range(n):
    w, h = map(int, input().split())
    peep.append((w, h))

for i in range(n):
    rank = 1
    for j in range(n):
        if peep[i][0] < peep[j][0] and peep[i][1] < peep[j][1]:
            rank += 1
    print(rank, end=' ')
