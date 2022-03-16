n = int(input())
tiles = list()
tiles.append(1)
tiles.append(2)
for i in range(2, n) :
	tiles.append((tiles[i-1] + tiles[i-2])%15746)

print(tiles[n-1])