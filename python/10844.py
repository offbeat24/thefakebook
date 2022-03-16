n = int(input())

num = [[0]*10 for _ in range(n)]

for i in range(1,10) :
	num[0][i] = 1

for i in range(1,n) :
	for j in range(10) :
		if j == 0 :
			num[i][j] = num[i-1][j+1]
		elif j == 9 :
			num[i][j] = num[i-1][j-1]
		else :
			num[i][j] = (num[i-1][j-1] + num[i-1][j+1])


print(sum(num.pop())%1000000000)
	