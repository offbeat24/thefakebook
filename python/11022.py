import sys
rl = sys.stdin.readline

t = int(rl())

for i in range(1, t+1) :
  a, b = map(int, rl().rstrip().split())
  sys.stdout.write(str("Case #") + str(i) + str(": ") + str(a) + str(" + ") + \
    str(b) + str(" = ") + str(a+b) + '\n')