import sys
rl = sys.stdin.readline

n, k = map(int, rl().rstrip().split())
cel = list(map(int, rl().rstrip().split()))
tmp = sum(cel[:k])
max_sum = tmp
for i in range(len(cel)-k) :
  tmp = tmp - cel[i] + cel[i+k]
  max_sum = max(tmp, max_sum)

print(max_sum)