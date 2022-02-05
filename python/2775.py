k = int(input())


for i in range(k):
    peep = 0
    a = int(input())
    b = int(input())
    floor = [n for n in range(1, b+1)]
    for j in range(0, a):
        for k in range(1, b):
            floor[k] += floor[k-1]

    print(floor[b-1])
