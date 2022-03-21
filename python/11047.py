n, k = map(int, input().split())

cost = list()
for _ in range(n):
    cost.append(int(input()))
cost.append(float('inf'))
cost.reverse()
answer = 0
for i in range(n):
    if k == 0:
        break
    if cost[i+1] <= k < cost[i]:
        answer += k // cost[i+1]
        k %= cost[i+1]
        continue

print(answer)
