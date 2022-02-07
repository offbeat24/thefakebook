brow = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
wrow = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

bchess = [brow, wrow, brow, wrow, brow, wrow, brow, wrow]
wchess = [wrow, brow, wrow, brow, wrow, brow, wrow, brow]


size = list(map(int, input().split()))

chess = [list(input()) for _ in range(size[0])]

data = list()
def btest(x, y) :
    cnt = 0;
    for i in range(x, x+8) :
        for j in range(y, y+8) :
            if bchess[i-x][j-y] != chess[i][j] :
                cnt += 1
    data.append(cnt)
    return

def wtest(x, y) :
    cnt = 0;
    for i in range(x, x+8) :
        for j in range(y, y+8) :
            if wchess[i-x][j-y] != chess[i][j] :
                cnt += 1
    data.append(cnt)
    return

for i in range(size[0]-7) :
    for j in range(size[1]-7) :
        btest(i, j)
        wtest(i, j)

print(min(data))