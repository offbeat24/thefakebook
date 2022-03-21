seq = list(input().split('-'))

num = list()
for i in seq:
    tmp = 0
    s = i.split('+')
    for j in s:
        tmp += int(j)
    num.append(tmp)

answer = num[0]
for i in range(1, len(num)):
    answer -= num[i]

print(answer)
