import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N = int(input().rstrip())

paint = list()
for _ in range(N) :
  paint.append(list(input().rstrip()))

visited = [[False] * N for _ in range(N)]

normal, blind = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(i, j) :
  visited[i][j] = True
  color = paint[i][j]
  
  for k in range(4) :
    x = i + dx[k]
    y = j + dy[k]
    
    if (0 <= x < N) and (0 <= y < N) :
      if visited[x][y]  == False:
        if paint[x][y] == color :
          dfs(x,y)

for i in range(N) :
  for j in range(N) :
    if visited[i][j] == False :
      dfs(i,j)
      normal += 1
        
for i in range(N) :
  for j in range(N) :
    if paint[i][j] =='R' :
      paint[i][j] = 'G'

visited = [[False] * N for _ in range(N)]

for i in range(N) :
  for j in range(N) :
    if visited[i][j] == False :
      dfs(i,j)
      blind += 1
      
print(normal, blind)