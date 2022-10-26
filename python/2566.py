matr = list()

for _ in range(9) :
  matr.append(list(map(int,input().split())))
  
ans = -1
ix = [-1, -1]
for i in range(9) :
  for j in range(9) :
    if matr[i][j] > ans :
      ans = matr[i][j]
      ix[0] = i
      ix[1] = j

print(ans)
print(ix[0]+1, ix[1]+1)