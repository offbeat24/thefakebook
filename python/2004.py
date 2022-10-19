def countNum(num, div) :
  ans = 0
  while num != 0 :
    num = num // div
    ans += num
  return ans
  
n, m = map(int, input().split())

if m == 0 :
  print(0)
  
else :
  print(min(countNum(n, 2) - countNum(m, 2) - countNum(n - m, 2) , countNum(n, 5) - countNum(m, 5) - countNum(n-m, 5)))
