from collections import deque
N, M = map(int, input().split())

ladder = dict()
snake = dict()

for _ in range(N) :
  f, t = map(int, input().split())
  ladder[f] = t
for _ in range(M) :
  f, t = map(int, input().split())
  snake[f] = t
  
visited = [False] * 101

q = deque([1])
board = [0] * 101

while q :
  loc = q.popleft()
  if loc == 100:
    print(board[loc])
    break
  for dice in range(1,7) :
    next_loc = loc + dice
    
    if next_loc <= 100 and not visited[next_loc] :
      if next_loc in ladder.keys():
        next_loc = ladder[next_loc]
      if next_loc in snake.keys():
        next_loc = snake[next_loc]
      if not visited[next_loc] :
        visited[next_loc] = True
        board[next_loc] = board[loc] + 1
        q.append(next_loc)