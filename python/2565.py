n = int(input())

lines = list()
for _ in range(n):
    line = list(map(int, input().split()))
    lines.append(line)

lines.sort()

lis = [0] * n

for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1] and lis[i] < lis[j]:
            lis[i] = lis[j]
    lis[i] += 1

print(n - max(lis))
