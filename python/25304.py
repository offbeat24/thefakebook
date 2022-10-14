import sys

wallet = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
rPrice = 0
for _ in range(n) :
  price , cnt = map(int, sys.stdin.readline().rstrip().split())
  rPrice += (price*cnt)
if wallet == rPrice :
  print("Yes")
else :
  print("No")