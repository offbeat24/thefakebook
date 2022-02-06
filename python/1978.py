n = int(input())

num = list(map(int, input().split()))


def primefinder(test):
    tmp = 0
    if test == 1:
        return 0
    for a in range(1, test+1):
        if test % a == 0:
            tmp += 1
            if tmp > 2:
                return 0
    return 1


cnt = 0

for i in num:
    cnt += primefinder(i)

print(cnt)
