from collections import deque
import sys
n = int(input())
q = deque()
for _ in range(n) :
  inp = sys.stdin.readline().rstrip().split()
  command = inp[0]
  if "push" == command :
    x = inp[1]
    q.append(int(x))
  elif "pop" == command :
    if len(q) :
      print(q.popleft())
    else : print(-1)
  elif "size" == command :
    print(len(q))
  elif "empty" == command :
    if len(q) :
      print(0)
    else :
      print(1)
  elif "front" == command :
    if len(q) :
      print(q[0])
    else :
      print(-1)
  elif "back" == command :
    if len(q) :
      print(q[-1])
    else :
      print(-1)