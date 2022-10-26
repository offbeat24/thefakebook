self_num = [0] * 10000

def sNum(a,b,c,d) :
  global self_num
  n = 1001*a + 101*b + 11*c + 2*d
  if n < 10000 :
    self_num[n] += 1

for aa in range(10) :
  for bb in range(10) :
    for cc in range(10) :
      for dd in range(10) :
        sNum(aa, bb, cc, dd)

for i in range(1, 10000) :
  if self_num[i] == 0 :
    print(i)