n = int(input())

for i in range(1, n) :
  ans = i
  tmp = i
  while tmp > 0 :
    ans += (tmp%10)
    tmp //= 10
  
  if ans == n :
    print(i)
    exit(0)
else :
  print(0)