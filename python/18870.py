n = int(input())

x_input = list(map(int, input().split()))

x_set = sorted(list(set(x_input)))


x_output = {x_set[i]: i for i in range(len(x_set))}

for i in x_input:
    print(x_output[i], end=" ")
