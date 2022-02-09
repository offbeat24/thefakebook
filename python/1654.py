k, n = map(int, input().split())

lan = list()

for _ in range(k):
    lan.append(int(input()))


l = 1
r = max(lan)
unit = 0
while l <= r:
    unit = (l + r) // 2
    cnt = 0
    for i in lan:
        cnt += i // unit
    if cnt >= n:
        l = unit + 1
    else:
        r = unit - 1

print(r)
