from collections import deque


n, k = input().split()
n = int(n)
k = int(k)

jose = deque(range(1, n+1))

print('<', end='')
while 1:
    for _ in range(k-1):
        jose.append(jose[0])
        jose.popleft()
    print(jose.popleft(), end='')
    if len(jose) == 0:
        print('>')
        break
    else:
        print(',', end=' ')
