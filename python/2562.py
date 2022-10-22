maxi = 0
t = 0

for i in range(1,10) :
  num = int(input())
  if num > maxi :
    t = i
    maxi = num

print(maxi, t, sep = "\n")
  
