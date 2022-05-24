a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

if n == 1 :
    print(a)
    exit()
elif n == 2 :
    answer = a*m + d
else :
    answer = a*m + d
    for _ in range(n-2) :
        answer = answer*m + d
    
print(answer)