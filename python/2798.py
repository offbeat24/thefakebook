n, m = map(int, input().split())

card = list(map(int, input().split()))
card.sort()
ans = 0
for i in range(len(card)-2) :
  for j in range(i+1, len(card)-1) :
    for k in range(j+1, len(card)) :
      s = card[i] + card[j] + card[k]
      if m >= s > ans :
        ans = s

print(ans)