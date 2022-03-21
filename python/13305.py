n = int(input())

dist = list(map(int, input().split()))

cost = list(map(int, input().split()))

tmp_cost = cost[0]
answer = tmp_cost * dist[0]
for i in range(1, n-1):
    if tmp_cost >= cost[i]:
        tmp_cost = cost[i]
    answer += tmp_cost * dist[i]

print(answer)
