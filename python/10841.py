n = int(input())
mem = []
for _ in range(n):
    mem.append(list(input().split()))

mem.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(mem[i][0], mem[i][1])
