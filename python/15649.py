n, m = map(int, input().split())

out = list()


def nnm():
    if len(out) == m:
        print(' '.join(map(str, out)))
        return
    for i in range(1, n+1):
        if i not in out:
            out.append(i)
            nnm()
            out.pop()


nnm()
