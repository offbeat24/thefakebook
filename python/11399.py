n = int(input())

peep = list(map(int, input().split()))

peep.sort()

answer = list()
answer.append(peep[0])
for i in range(1, n):
    answer.append(answer[i-1] + peep[i])

print(sum(answer))
