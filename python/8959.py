import sys
rl = sys.stdin.readline

n = int(rl())

for _ in range(n) :
  ox = list(rl().rstrip())
  flag = 0
  score = 0
  for c in ox :
    if c == "O" :
      flag += 1
      score += flag
    elif c == "X" :
      flag = 0
  print(score)

