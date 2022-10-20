n, m = map(int, input().split())
num = list(map(int, input().split()))
sum_num = [num[0]]
r_idx = [0] * m
for i in range(1, len(num)) :
  sum_num.append(sum_num[i-1] + num[i])
  r_idx[sum_num[i-1]%m] += 1

r_idx[sum_num[-1]%m] += 1

ans = 0
for cnt in r_idx :
  if cnt > 0 :
    ans += (cnt)*(cnt-1)//2
ans += r_idx[0]
print(ans)