import heapq


h1 = [1, 3, 5, 7, 9]
h2 = [2, 4, 6, 8, 0]

heapq.heapify(h1)
heapq.heapify(h2)

h1 += h2

heapq.heapify(h1)
print(h1)
