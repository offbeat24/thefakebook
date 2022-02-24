a, b, c = map(int, input().split())


if c <= b:
    print(-1)
    exit(0)

print((a // (c-b)) + 1)
