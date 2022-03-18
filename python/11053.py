n = int(input())

arr = list(map(int, input().split()))

lis = [0] * n

for i in range(n) :
	for j in range(i) :
		if arr[i] > arr[j] and lis[i] < lis[j] :
			lis[i] = lis[j]
	lis[i] += 1
print(max(lis))