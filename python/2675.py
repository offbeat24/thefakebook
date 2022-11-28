n = int(input())

for _ in range(n) :
  t, word = input().split()
  t = int(t)
  ans = list()
  for c in word :
    for _ in range(t) :
      ans.append(c)
  print(*ans, sep = "")