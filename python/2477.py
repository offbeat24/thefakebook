import sys

melon = int(sys.stdin.readline().rstrip())
rec_dir = list()
rec_len = list()
for i in range(6) :
  rec_dir[i], rec_len[i] = map(int, sys.stdin.readline().rstrip().split())
  
