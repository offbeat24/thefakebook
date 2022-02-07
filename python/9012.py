n = int(input())


def vps_test(sample):
    test = 0
    for p in sample:
        if p == '(':
            test += 1
        elif p == ')':
            test -= 1
            if test < 0:
                return test
    return test


for _ in range(n):
    ps = list(input())
    if vps_test(ps) == 0:
        print('YES')
    else:
        print('NO')
