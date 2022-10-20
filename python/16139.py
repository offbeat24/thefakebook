from string import ascii_lowercase
import sys
import copy
rl = sys.stdin.readline

alpha = list(ascii_lowercase)
s = rl().rstrip()
q = int(rl())

al_idx = [[0] * len(alpha) for _ in range(2)]
al_idx[0][ord(s[0]) - ord('a')] += 1
al_idx[1][ord(s[0]) - ord('a')] += 1
for i in range(1, len(s)) :
  al_idx[i][ord(s[i]) - ord('a')] += 1
  tmp = copy.deepcopy(al_idx[i])
  al_idx.append(tmp)
  
for _ in range(q) :
  c, l, r = rl().rstrip().split()
  l = int(l)
  r = int(r)
  if l == 0 :
    ans = al_idx[r][ord(c)-ord('a')]
  else :
    ans = al_idx[r][ord(c)-ord('a')] - al_idx[l-1][ord(c)-ord('a')]
  sys.stdout.write(str(ans) + '\n')