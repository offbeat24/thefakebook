#!/bin/python3

from collections import deque
import math
import os
import random
import re
import sys



#
# Complete the 'findMinimumTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. UNWEIGHTED_INTEGER_GRAPH centre
#  2. INTEGER_ARRAY status
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#
def findMinimumTime(centre_nodes, centre_from, centre_to, status, edges):
  sur = list()
  defi = list()
  suf = list()
  graph = [[] for _ in range(len(status)+1)]
  ans = list()

  for i in range(len(status)) :
    if status[i] == 3 :
      sur.append(i+1)
    elif status[i] == 2 :
      suf.append(i+1)
    else :
      defi.append(i+1)
  for i in range(edges) :
    graph[centre_to[i]].append(centre_from[i])
    graph[centre_from[i]].append(centre_to[i])
  
  dist = list()
  for d in defi :
    visited = [False] * (centre_nodes+1)
    q = deque([(d,0)])
    visited[d] = True
    while q:
      now, n = q.popleft()
      if now in sur :
        dist.append(n)
        break
      for i in graph[now] :
        if not visited[i] :
          q.append((i,n+1))
          visited[i] = True
  
  return(max(dist))

if __name__ == '__main__':

    centre_nodes, centre_edges = map(int, input().rstrip().split())

    centre_from = [0] * centre_edges
    centre_to = [0] * centre_edges

    for i in range(centre_edges):
        centre_from[i], centre_to[i] = map(int, input().rstrip().split())

    status_count = int(input().strip())

    status = []

    for _ in range(status_count):
        status_item = int(input().strip())
        status.append(status_item)

    result = findMinimumTime(centre_nodes, centre_from, centre_to, status, centre_edges)

    print(str(result) + '\n')

fptr = open(os.environ['OUTPUT_PATH'], 'w')

fptr.write(result + '\n')

fptr.close()