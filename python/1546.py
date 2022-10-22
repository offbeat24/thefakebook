n = int(input())
sc = list(map(int, input().split()))

m = max(sc)

print((sum(sc)*100)/m/n)