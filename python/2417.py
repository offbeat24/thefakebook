import math


n = int(input())

left = 0
right = n
mid = (left+right) // 2

while left <= right:

    if mid**2 > n:
        right = mid-1

    elif mid**2 < n:
        left = mid+1

    else:
        break
    mid = math.ceil((left+right) / 2)

print(mid)
