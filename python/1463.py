n = int(input())

arr = [0] * (n+1)

for i in range(2, n+1):
    a = float('inf')
    b = float('inf')
    if i % 2 == 0:
        a = arr[i//2]+1
    if i % 3 == 0:
        b = arr[i//3]+1
    arr[i] = min(arr[i-1] + 1, a, b)

print(arr[n])
