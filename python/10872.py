n = int(input())
if n == 0 :
    print(1)
    exit(0)


def fact(num) :
    global mul
    if num == n :
        print(mul*n)
    else :
        mul *= num
        fact(num+1)
mul = 1
fact(1)