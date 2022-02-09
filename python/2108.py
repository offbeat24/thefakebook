import sys
from typing import Counter


n = int(input())

data = list(int(sys.stdin.readline()) for _ in range(n))

data.sort()

cnt = Counter(data).most_common()


print(round(sum(data)/n))
print(data[n//2])
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(max(data)-min(data))
