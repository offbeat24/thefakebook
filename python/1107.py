N = int(input())
ans = abs(N - 100)
M = int(input())

if M :
  broken = list(input().split())
else : 
  broken = list()



for num in range(1000001) :
  for tmp in str(num) :
    if tmp in broken :
      break
  else :
    ans = min(ans, len(str(num)) + abs(num-N))

print(ans)
    