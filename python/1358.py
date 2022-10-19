import sys

w, h, x, y, p = map(int, sys.stdin.readline().rstrip().split())
r = h // 2
player = 0
for _ in range(p) :
  x1, y1 = map(int, sys.stdin.readline().rstrip().split())
  if y1 > y + h  or y1 < y :
    continue
  if x1 > x + w :
    if (x+w-x1)**2 + (y+r-y1)**2 <= r**2 :
      player += 1
      continue
  elif x1 < x :
    if (x-x1)**2 + (y+r-y1)**2 <= r**2 :
      player += 1
      continue
  else :
    player += 1

print(player)