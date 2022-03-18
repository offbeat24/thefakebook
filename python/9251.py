sub1 = list(input().strip())
sub2 = list(input().strip())

lcs = [[0] * (len(sub2) + 1) for _ in range(len(sub1)+1)]

for i in range(1, len(sub1)+1):
    for j in range(1, len(sub2)+1):
        if sub1[i-1] == sub2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[-1][-1])
