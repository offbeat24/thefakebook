from collections import deque
M, N, H = map(int, input().split())

tomato = list()

for _ in range(H) :
  tmp = list()
  for _ in range(N) :
    tmp.append(list(map(int, input().split())))
  tomato.append(tmp)

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(tomamto, m, n, h) :
  q = deque()
  
  for i in range(h): 
    for j in range(n) :
      for k in range(m) :
        if tomamto[i][j][k] == 1:
          q.append([i,j,k,0])
  while q :
    z, y, x, d = q.popleft()
    for i in range(6) :
      if (0 <= z+dz[i] < h) and (0 <= y+dy[i] < n) and (0 <= x+dx[i] < m) :
        if tomamto[z+dz[i]][y+dy[i]][x+dx[i]] == 0 :
          q.append([z+dz[i], y+dy[i], x+dx[i], d+1])
          tomamto[z+dz[i]][y+dy[i]][x+dx[i]] = d+1
  
  ans = 0
  flat_tomato = [k for i in tomamto for j in i for k in j]

  if 0 in flat_tomato :
    return -1
  else :
    ans = max(max(flat_tomato), ans)
    if ans == 1 :
      return 0
    return ans
  
print(bfs(tomato, M, N, H))