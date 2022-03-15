n, m = map(int, input().split())

out = list()


def nnm(sp):
    if len(out) == m:
        print(' '.join(map(str, out)))
        return
    for i in range(sp, n+1):
        if i not in out:
            out.append(i)
            nnm(i+1)
            out.pop()


nnm(1)
