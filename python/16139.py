from string import ascii_lowercase
import sys
rl = sys.stdin.readline
alpha = list(ascii_lowercase)
al_idx = list()
s = rl().rstrip()
q = int(rl())

for idx, i in enumerate(alpha) :
  tmp = list()
  for c in range(len(s)) :
    if s[c] == i :
      tmp.append(c)
  al_idx.append(tmp)

for _ in range(q) :
  ques = list(rl().rstrip().split())
  ans = 0
  al = ques[0]
  l , r = map(int, ques[1:])
  for i in al_idx[ord(al) - ord('a')] :
    if i < l : 
      continue
    if l <= i <= r :
      ans += 1
    if r < i :
      break
  sys.stdout.write(str(ans) + '\n')