import sys

n , m = map(int , sys.stdin.readline().rstrip().split())

heardX = set()
seenX = set() 

for _ in range(n) :
  heardX.add(sys.stdin.readline().rstrip())
  
for _ in range(m) :
  seenX.add(sys.stdin.readline().rstrip())
  
unknown = heardX & seenX
ans = list(unknown)
ans.sort()
print(len(ans))
print(*ans, sep = "\n")