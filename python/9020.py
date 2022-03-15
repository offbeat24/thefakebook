from collections import deque
import sys


def is_prime(num) :
    if num == 1 :
        return False
    for i in range(2, num) :
        if num % i == 0 :
            return False
    else :
        return True

n = int(input())
input_array = deque()
for _ in range(n) :
    input_array.append(int(sys.stdin.readline()))
    
while input_array :
    gold = input_array.popleft()
    #max_prime = 0
    for i in range((gold//2) - 1, gold) :
        if is_prime(i) and is_prime(gold-i) :
            #max_prime = max(i, max_prime)
            answer = [i, gold-i]
            answer.sort()
            print(answer[0], answer[1])
            break
    #print(max_prime, gold - max_prime)