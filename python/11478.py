import sys

word = sys.stdin.readline().rstrip()
strset = set()
for i in range(1,len(word)) :
  start = 0
  while start + i <= len(word) :
    strset.add(word[start:start+i])
    start += 1

print(len(strset)+1)