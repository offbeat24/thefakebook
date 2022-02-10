while 1:
  i = input()
  if i == '.' :
    break
  ps = list()
  for c in i :
    if c == '(' or c == '[' :
      ps.append(c)
    elif c == ')' :
      if len(ps) != 0 :
        p = ps.pop()
        if p == '(' :
          continue
        else :
          ps.append(p)
          break
      else :
        ps.append(0)
        break
    elif c == ']' :
      if len(ps) != 0 :
        p = ps.pop()
        if p == '[' :
          continue
        else :
          ps.append(p)
          break
      else :
        ps.append(0)
        break
  if len(ps) :
    print('no')
    continue
  print('yes')
