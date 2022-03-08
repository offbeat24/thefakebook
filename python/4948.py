import sys


def is_prime(num) :
    for i in range(2, int(num**0.5)+1) :
        if num % i == 0:
            return 0
    else :
        return 1
    
while True :
    n = int(sys.stdin.readline())
    if n == 0 :
        break
    answer = 0
    for i in range(n+1, 2*n+1) :
        answer += is_prime(i)
    
    print(answer)