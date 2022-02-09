import sys


n = int(input())

num = list(0 for _ in range(10001))

for _ in range(n):
    num[int(input())] += 1

for i in range(1, 10001):
    for j in range(num[i]):
        print(i)
