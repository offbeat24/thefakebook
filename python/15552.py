import sys
rl = sys.stdin.readline

t = int(rl())

for _ in range(t) :
  a, b = map(int, rl().rstrip().split())
  sys.stdout.write( str(a+b) + '\n')