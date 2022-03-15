from os import sep


n = int(input())

sij = list()
for _ in range(n):
    row = list(map(int, input().split()))
    sij.append(row)


team = [0] * n
answer = float('inf')


def calc():
    start = 0
    link = 0
    for i in range(n):
        for j in range(n):
            if team[i] and team[j]:
                start += sij[i][j]
            if not team[i] and not team[j]:
                link += sij[i][j]
    return abs(start - link)


def seperating(depth, idx):
    global answer
    if depth == n//2:
        answer = min(answer, calc())
        if not answer:
            print(answer)
            exit(0)
        return
    for i in range(idx, n):
        if team[i] == 0:
            team[i] = 1
            seperating(depth+1, i+1)
            team[i] = 0


seperating(0, 0)
print(answer)
