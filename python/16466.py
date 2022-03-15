import heapq
from queue import PriorityQueue


n = int(input())

sold_ticket = list(map(int,input().split()))

heapq.heapify(sold_ticket)

