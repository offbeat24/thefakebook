import heapq

T = int(input())

for _ in range(T) :
  k = int(input())
  visited = [False] * k
  max_h = list()
  min_h = list()
  for i in range(k) :
    cmd, num = input().split()
    num = int(num)
    
    if cmd == "I":
      heapq.heappush(min_h, (num,i))
      heapq.heappush(max_h, (-1*num, i))
      visited[i] = True
    elif num == 1 :
      while max_h and not visited[max_h[0][1]] :
        heapq.heappop(max_h)
      if max_h:
        visited[max_h[0][1]] = False
    else :
      while min_h and not visited[min_h[0][1]] :
        heapq.heappop(min_h)
      if min_h:
        visited[min_h[0][1]] = False
  while min_h and not visited[min_h[0][1]] :
    heapq.heappop(min_h)
  while max_h and not visited[max_h[0][1]] :
    heapq.heappop(max_h)
  print(-1*max_h[0][0], min_h[0][0]) if max_h and min_h else print("EMPTY")