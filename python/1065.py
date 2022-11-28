n = int(input())

def hansu(num) :
  tmp = str(num)
  sl_num = list(map(int, tmp))
  if len(sl_num) == 1 or len(sl_num) == 2:
    return 1
  elif len(sl_num) == 3 :
    if sl_num[0] + sl_num[2]== sl_num[1]*2 :
      return 1
    return 0
  else :
    return 0

cnt = 0
for i in range(1,n+1) :
  cnt += hansu(i)

print(cnt)