import sys

T = int(input())

for _ in range(T) :
  n = int(input())
  if n == 0 : 
    print(n)
    continue
  ans = 1
  closet = dict()
  for _ in range(n) :
    _, kind = sys.stdin.readline().rstrip().split()
    if kind in closet : 
      closet[kind] += 1
    else : 
      closet[kind] = 1
  for cloth in closet.values() :
    ans *= cloth + 1
  print(ans - 1)