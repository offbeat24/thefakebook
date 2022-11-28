def starDraw(k) :
  if k == 1 :
    return ["*"]
  
  star = starDraw(k//3)
  tmp = list()
  for s in star :
    tmp.append(s*3)
  for s in star :
    tmp.append(s+' '*(k//3) + s)
  for s in star :
    tmp.append(s*3)
  return tmp

n = int(input())

print('\n'.join(starDraw(n)))