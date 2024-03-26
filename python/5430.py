import sys
input = sys.stdin.readline
T = int(input())


for _ in range(T) :
  cmd = list(input().rstrip())
  n = int(input().rstrip())
  xx = input().strip()
  if xx == "[]" :
    x = list()
  else :
    x = list(xx.lstrip('[').rstrip(']').split(','))
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