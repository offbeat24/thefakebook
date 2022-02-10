from collections import deque
c = int(input())

for i in range(c) :
  n, m = map(int, input().split())
  q = list(map(int, input().split()))
  dq = deque(q)
  cnt = 0
  while 1:
    if dq[0] < max(dq) : 
      dq.append(dq.popleft())
      m -= 1
      if m < 0 :
        m = len(dq) - 1
    else :
      dq.popleft()
      if m == 0 :
        cnt += 1
        print(cnt)
        break
      else :
        cnt += 1
        m -= 1


