n = int(input())
m = int(input())

def is_prime(num) :
  if num == 1:
    return False
  for i in range(2, num) :
    if num % i == 0 :
      return False 
  return True 

sum_ = list()

for i in range(n, m+1) :
  if is_prime(i) :
    sum_.append(i)

if len(sum_) == 0 :
  print(-1)
else :
  print(sum(sum_))
  print(sum_[0])
      
