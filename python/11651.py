n = int(input())

data = list()
for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])

data.sort(key=lambda x: x[0])
data.sort(key=lambda x: x[1])

for i in range(n):
    print(data[i][0], data[i][1])
