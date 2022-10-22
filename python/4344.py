from collections import deque
import sys
rl = sys.stdin.readline

c = int(rl().rstrip())

for _ in range(c) :
  inp = deque(map(int, rl().rstrip().split()))
  n = inp.popleft()
  avg = sum(inp) / n
  cnt = 0
  for score in inp :
    if score > avg :
      cnt += 1
  
  print("{:.3f}%".format(cnt*100/n))