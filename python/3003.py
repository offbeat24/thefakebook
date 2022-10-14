import sys

input =  list(map(int, sys.stdin.readline().rstrip().split()))
chess = [1, 1, 2, 2, 2, 8]

for i in range(6) :
  print(chess[i] - input[i], end = ' ')