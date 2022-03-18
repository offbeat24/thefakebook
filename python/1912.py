n = int(input())

arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]
for i in range(n-1):
    dp[i+1] = max(dp[i] + arr[i+1], arr[i+1])
print(max(dp))
