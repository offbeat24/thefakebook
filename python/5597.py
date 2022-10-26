student = [False] * 31

for _ in range(28) :
  student[int(input())] = True

cnt = 0
for i in range(1,31) :
  if student[i] == False :
    print(i)
    cnt += 1
    if cnt == 2 :
      break

