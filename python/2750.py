n = int(input())
nums = list()
for _ in range(n) :
  nums.append(int(input()))
nums.sort()
print(*nums, sep = "\n")