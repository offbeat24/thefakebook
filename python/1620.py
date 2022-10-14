import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

pokemon = list()

for _ in range(n) :
  pokemon.append(sys.stdin.readline().rstrip())
  
for _ in range(m) :
  quiz = sys.stdin.readline().rstrip()
  if quiz.isdigit() :
    print(pokemon[int(quiz)-1])
  else :
    print(pokemon.index(quiz)+1)