n, m = map(int, input().split())

weight = list(map(int, input().split()))

def isPrime(num) :
  if num < 2 :
    return False
  else :
    for i in range(2, num) :
      if num % i == 0 :
        return False
    return True 

ans = set()
visited = [False] * n
def cow(l, d, cow_weight) :
  global visited
  global ans
  if d == m :
    if isPrime(cow_weight) :
      ans.add(cow_weight)
  for i in range(l, n) :
    if not visited[i] :
      visited[i] = True
      cow(l+1, d+1, cow_weight + weight[i])
      visited[i] = False

cow(0,0,0)

answer = list(ans)
answer.sort()
#print(answer)
if answer:
  for i in answer :
    print(i, end = ' ')
else :
  print(-1)