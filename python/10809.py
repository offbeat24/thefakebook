word = input()

for i in range(26) :
  try:
    print(word.index(chr(97+i)))
  except:
    print(-1)