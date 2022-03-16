import heapq


n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)
for _ in range(n-1):
    num = list(map(int, input().split()))

    for i in num:
        if i > heap[0]:
            heapq.heappush(heap, i)
            heapq.heappop(heap)

print(heapq.heappop(heap))
