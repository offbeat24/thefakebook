import sys
from collections import deque
rl = sys.stdin.readline

n, m = map(int, rl().rstrip().split())
target = list(map(int, rl().rstrip().split()))
q = deque([i for i in range(1, n+1)])
for t in target :
  if t <= n // 2 :
    q.rotate(-1)
  else :
    q.rotate(1)
