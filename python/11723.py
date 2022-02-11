n = int(input())

s = set()
for _ in range(n):
    ord = list(input().split())

    if ord[0] == 'add':
        s.add(ord[1])
    elif ord[0] == 'remove':
        try:
            s.remove(ord[1])
        except:
            continue
    elif ord[0] == 'check':
        if ord[1] in s:
            print(1)
        else:
            print(0)
    elif ord[0] == 'toggle':
        if ord[1] in s:
            s.remove(ord[1])
        else:
            s.add(ord[1])
    elif ord[0] == 'all':
        s = set(list(i for i in range(1, 21)))
    elif ord[0] == 'empty':
        s.clear()
