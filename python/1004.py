import sys

T = int(sys.stdin.readline().rstrip())


for _ in range(T) :
  x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())

  n = int(sys.stdin.readline().rstrip())
  ans = 0
  for _ in range(n) :
    x, y, r = map(int, sys.stdin.readline().rstrip().split())
    in_flag_start = (True if ((x1-x)**2 + (y1-y)**2 < r**2) else False)
    in_flag_end = (True if ((x2-x)**2 + (y2-y)**2 < r**2) else False)
    
    if in_flag_start != in_flag_end : 
      ans += 1
    else : continue
  print(ans)
