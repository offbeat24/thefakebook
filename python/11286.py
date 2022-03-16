import heapq
import sys


n = int(input())

heap = list()

for _ in range(n) :
    ord = int(sys.stdin.readline())
    if not ord :
        try :
            print(heapq.heappop(heap)[1])
        except :
            print(0)
    else :
        heapq.heappush(heap, (abs(ord), ord))
