n = int(input())

tile = [0, 1, 2]
if n == 1 or n == 2 :
  print(tile[n])
  exit(0)
for i in range(3, n+1) :
  tile.append(tile[i-1] + tile[i-2])

print(tile[n]%10007)