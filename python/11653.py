n = int(input())
if n == 1:
    exit(0)
for num in range(2, n+1) :
    while num > 1:
        if n % num !=0 :
            break
        else : 
            n //= num
            print(num)
    else :
        break