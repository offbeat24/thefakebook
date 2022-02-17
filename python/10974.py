n = int(input())

def dfs() :
    if len(per) == n :
        for i in per :
            print(i, end=' ')
        print()
        return
    
    for i in range(1, n+1) :
        if i not in per :
            per.append(i)
            dfs()
            per.pop()
            
per = list()
dfs()