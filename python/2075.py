import heapq


n = int(input())

table = list()
for _ in range(n) :
    h = list()
    row = list(map(int,input().split()))
    for i in range(len(row)) :
        heapq.heappush(h, row[i]*-1)
    table.append(h)
    print(h)

heap = list()
for i in range(n) :
    heapq.heappush(heap, heapq.heappop(table[i]) * -1)

print(heapq.heappop(heap))