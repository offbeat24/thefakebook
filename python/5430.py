import sys
input = sys.stdin.readline
T = int(input())


for _ in range(T) :
  cmd = list(input().rstrip())
  n = int(input().rstrip())
  x = list(input().strip().lstrip('[').rstrip(']').split(','))
  st = 0
  en = len(x) - 1
  di = True
  for c in cmd :
    if c == "R" :
      di = not di
      continue
    elif c == "D" :
      if st > en :
        print("error")
        break
      else :
        if di :
          st += 1
        else :
          en -= 1
        continue
  else :
    if di :
      print("[" + ",".join(x[st:en+1]) + "]")
    else :
      print("[" + ",".join(reversed(x[st:en+1])) + "]")