wor = input()
word = wor.upper()

i = [0] * 26
for c in word :
  i[ord(c)-65] += 1

tmp = max(i)

if i.count(tmp) > 1 :
  print("?")
else :
  print(chr(i.index(tmp)+65))
  