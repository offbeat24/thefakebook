r_cnt = 0
d_cnt = 0

def fib(n) :
  global r_cnt
  if n == 1 or n == 2 :
    r_cnt += 1
    return 1
  else : return (fib(n-1) + fib(n-2));
  
def fiboDyna(n) :
  global d_cnt
  f = [ 0, 1, 1 ]
  for i in range(3, n+1):
    f.append(f[i-1] + f[i-2])
    d_cnt += 1
  return f[n]

num = int(input())


fib(num)
fiboDyna(num)

print(r_cnt, d_cnt)