t = int(input())

for _ in range(t) :
  h, w, n = map(int, input().split())
  
  print((n%h if n%h != 0 else h), str((n//h)+1 if n%h != 0 else n//h ).zfill(2), sep = "")