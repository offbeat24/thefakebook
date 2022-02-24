n = int(input())

depth = 0

while n > depth:
    n -= depth
    depth += 1

if depth % 2 == 0:
    print(n, '/', depth - n + 1, sep='')

else:
    print(depth - n + 1, '/', n, sep='')
