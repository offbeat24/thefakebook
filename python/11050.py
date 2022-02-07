import math


nk = list(map(int, input().split()))

print(int(math.factorial(nk[0]) /
      (math.factorial(nk[1])*math.factorial(nk[0]-nk[1]))))
