n = int(input())
if n == 0 :
    print(0)
    exit(0)
if n == 1 :
    print(1)
    exit(0)
def fibo(i) : 
    if i == n :
        print(answer[i-1] + answer[i-2])
        exit(0)
    else :
        answer.append(answer[i-1] + answer[i-2])
        fibo(i+1)

answer = [0, 1]

fibo(2)