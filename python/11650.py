n = int(input())

loc = list()
for i in range(n):
    loc.append(list(input().split()))

loc.sort(key=lambda x: int(x[1]))
loc.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(loc[i][0], loc[i][1])
