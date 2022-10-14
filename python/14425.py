import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

s = set()
for _ in range(n) :
  s.add(sys.stdin.readline().rstrip())

cnt = 0
for _ in range(m) :
  word = sys.stdin.readline().rstrip()
  if word in s :
    cnt += 1

print(cnt)