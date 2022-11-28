def hanoi(k, f, t, tmp) :
  global ans
  global cnt
  if k == 0 : return
  hanoi(k-1, f, tmp, t)
  ans.append(str(f) + ' ' + str(t))
  cnt += 1
  hanoi(k-1, tmp, t, f)
  
n = int(input())
cnt = 0
ans = list()

hanoi(n,1,3,2)
print(cnt)
print(*ans, sep="\n")
