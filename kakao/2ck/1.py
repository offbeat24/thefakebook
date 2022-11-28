flowers = [[3,4],[4,5],[6,7],[8,10]]

day = sum(flowers, [])

days = [0 for _ in range(max(day)+1)]

for f in flowers :
  a, b = f
  for i in range(a,b) :
    days[i] += 1
  
answer = 0 
for i in range(1, max(day) + 1) :
  if days[i] > 0 :
    answer += 1

print(answer)