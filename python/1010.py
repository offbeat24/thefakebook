import sys
import math

t = int(sys.stdin.readline().rstrip())

for _ in range(t) :
  m, n = map(int, sys.stdin.readline().rstrip().split())
  print(math.factorial(n) // (math.factorial(n-m) * math.factorial(m)))
  