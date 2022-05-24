table = list()
for _ in range(19):
    table.append(list(map(int, input().split())))

n = int(input())

for _ in range(n) :
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    for i in range(19) :
        if table[i][y] == 0:
            table[i][y] = 1
        else :
            table[i][y] = 0
    
    for i in range(19) :
        if table[x][i] == 0:
            table[x][i] = 1
        else :
            table[x][i] = 0
for row in table :
    print(*row, sep = " ")
