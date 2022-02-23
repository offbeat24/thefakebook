import sys


n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))


sum_list = [arr[0]]
for i in range(1, n):
    sum_list.append(arr[i] + sum_list[-1])

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())

    start -= 2
    end -= 1
    if start < 0:
        print(sum_list[end])
        continue
    print(sum_list[end] - sum_list[start])
