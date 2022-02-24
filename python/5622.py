num = list(input())

dial = [None, None, 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

answer = 0
for alpha in num:
    for i in range(2, 10):
        if alpha in dial[i]:
            answer += i+1

print(answer)
