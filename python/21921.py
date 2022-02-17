n , x= map(int, input().split())

graph = list(map(int, input().split()))

maxx = sum(graph[:x])
tmp = maxx
tmpp = 0
cnt = 1
for i in range(1,n-x+1) :
    tmpp = tmp - graph[i-1] + graph[i+x-1]
    
    if tmpp == maxx:
        cnt += 1
    elif tmpp > maxx :
        cnt = 1
        maxx = max(tmpp, maxx)
    
    tmp = tmpp

if maxx == 0 : 
    print("SAD")
else :
    print(maxx)
    print(cnt)