import heapq

n = int(input())

sold_ticket = list(map(int, input().split()))
heapq.heapify(sold_ticket)
tmp = heapq.heappop(sold_ticket)
idx = 0
while True:
    idx += 1
    if idx == tmp:
        try:
            tmp = heapq.heappop(sold_ticket)
        except:
            print(idx+1)
            exit(0)
        continue
    else:
        print(idx)
        exit(0)
