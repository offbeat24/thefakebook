n, m, b = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(n)]
hei = 0
ans = 128000000
for i in range(257):
    dig = 0
    top = 0
    for j in range(n):
        for k in range(m):
            if land[j][k] < i:
                top += (i - land[j][k])
            else:
                dig += (land[j][k] - i)
    inven = dig + b
    if inven < top:
        continue
    time = 2 * dig + top
    if time <= ans:
        ans = time
        hei = i
print(ans, hei)
