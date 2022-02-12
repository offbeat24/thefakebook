import sys


n = int(input())

s = set()
for _ in range(n):
    ord = list(sys.stdin.readline().split())

    if ord[0] == 'add':
        s.add(int(ord[1]))
    elif ord[0] == 'remove':
        try:
            s.remove(int(ord[1]))
        except:
            continue
    elif ord[0] == 'check':
        if int(ord[1]) in s:
            print(1)
        else:
            print(0)
    elif ord[0] == 'toggle':
        if int(ord[1]) in s:
            s.remove(int(ord[1]))
        else:
            s.add(int(ord[1]))
    elif ord[0] == 'all':
        s = set(range(1, 21))
    elif ord[0] == 'empty':
        s.clear()
