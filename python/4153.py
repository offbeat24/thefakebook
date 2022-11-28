while True:
  tri = list(map(lambda x: int(x)**2 , input().split()))
  tri.sort()
  if tri[0]==tri[1]==tri[2]==0:
    break
  if tri[2] == tri[1] + tri[0] :
    print("right")
  else:
    print("wrong")