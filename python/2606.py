from collections import deque


n = int(input())

c = int(input())

ord = list()

visit = [0] * (n+1)
visit[1] = 1
a = deque()
a.append(1)
for i in range(c):
    x, y = map(int, input().split())
    ord.append([x, y])
    ord.append([y, x])

ord.sort(key=lambda x: x[0])

while 1:
    for i in range(len(ord)):
        if ord[i][0] == a[0]:
            if visit[ord[i][1]] == 0:
                a.append(ord[i][1])
                visit[ord[i][1]] = 1
    a.popleft()
    if len(a) == 0:
        break

print(sum(visit) - 1)
