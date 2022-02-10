n, m = map(int, input().split())

tree = list(map(int, input().split()))


s = sum(tree)
l = 1
r = max(tree)
while l <= r :
  mid = (l + r) // 2
  data = 0
  for i in tree:
    if i >= mid :
      data += i - mid

  if data >= m :
    l = mid + 1 
  else :
    r = mid - 1

print(r)
