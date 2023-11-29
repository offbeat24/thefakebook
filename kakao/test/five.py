MOD = 10007

def solution(n, tops):
    cnt =0
    for i in tops:
      if i == 1:
        cnt += 1
    c = 2*n + 1
    dp = [0] * (c + 1)
    dp[0] = 1  # 합이 0이 되는 경우의 수는 1 (아무것도 선택하지 않는 경우)

    # 1과 2를 사용하여 각 숫자를 만드는 경우의 수 계산
    for i in range(1, c + 1):
        if i >= 1:
            dp[i] += dp[i - 1]
        if i >= 2:
            dp[i] += dp[i - 2]

    return (dp[c]+(n*cnt))%MOD

# 예시: n = 5
for n in range(1, 10) :
  print(solution(n, 1))
