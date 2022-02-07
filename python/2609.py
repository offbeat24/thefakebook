num = list(map(int, input().split()))
num.sort(reverse=True)
num2 = num
lcm = num[0] * num[1]
print(num2)
gcd = 0
while 1 :
    tmp = 0;
    if num[0] % num[1] == 0 :
        gcd = num[1]
        break
    else :
        tmp = num[0] % num[1]
        num[0] = num[1]
        num[1] = tmp
print(num2)
print(gcd)

lcm /= gcd

print(int(lcm))

#num 왜 동기화 됨?
