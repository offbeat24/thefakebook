n, k = map(int, input().split())

stuff = [[0, 0]]
for _ in range(n):
    wv = list(map(int, input().split()))
    stuff.append(wv)

sack = [[0] * (k+1)for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        w = stuff[i][0]
        v = stuff[i][1]

        if j < w:
            sack[i][j] = sack[i-1][j]
        else:
            sack[i][j] = max(v + sack[i-1][j-w], sack[i-1][j])

print(sack[n][k])
