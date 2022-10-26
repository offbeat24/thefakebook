paper = [[0]*100 for _ in range(100)]

n = int(input())

for _ in range(n) :
  x, y = map(int, input().split())
  for i in range(y, y+10) :
    for j in range(x, x+10) :
      paper[i][j] += 1
cnt = 0      
for p in paper :
  cnt += p.count(0)
  
print(10000 - cnt)