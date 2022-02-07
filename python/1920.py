n = int(input())

sample = list(map(int, input().split()))

size = int(input())

test = list(map(int, input().split()))

for num in test:
    if num in sample:
        print(1)
    else:
        print(0)
