n = int(input())

arr = list(map(int, input().split()))

lis = [0] * n
sil = [0] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and lis[i] < lis[j]:
            lis[i] = lis[j]
    lis[i] += 1
arr.reverse()
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and sil[i] < sil[j]:
            sil[i] = sil[j]
    sil[i] += 1

answer = [0] * n
sil.reverse()
for i in range(n):
    answer[i] = lis[i] + sil[i] - 1
print(max(answer))
