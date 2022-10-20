import sys
from collections import deque
rl = sys.stdin.readline

n, m = map(int, rl().rstrip().split())
target = list(map(int, rl().rstrip().split()))
q = deque([i for i in range(1, n+1)])
move = 0
for t in target:
  if t == q[0]:
    q.popleft()
    continue
  l = q.index(t)
  r = len(q) - l

  if l <= r:
    q.rotate(-l)
    q.popleft()
    move += l
  else: 
    q.rotate(r)
    q.popleft()
    move += r

print(move)
