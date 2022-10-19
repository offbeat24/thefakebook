import sys 

n = int(sys.stdin.readline().rstrip())

rings = list(map(int, sys.stdin.readline().rstrip().split()))
def gcd(a, b) :
  while (b != 0):
    n = a % b
    a = b
    b = n
  return a
    
for i in range(1, n) :
  g = gcd(rings[0], rings[i])
  print('{0}/{1}'.format(rings[0]//g, rings[i]//g))