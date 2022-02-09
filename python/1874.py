from collections import deque


n = int(input())

target = list(int(input()) for _ in range(n))

sample = deque(range(1, n+1))

output = list()
output.append(0)
ans = list()
ans.append(0)
for num in target:
    flag = 0
    while len(output) > 0:
        if output[-1] == num:
            ans.append('-')
            output.pop()
            flag = 1
            break
        else:
            try:
                output.append(sample.popleft())
            except:
                break
            ans.append('+')
            continue

    if flag:
        ans[0] = 1
    else:
        ans[0] = 0
        break
if ans[0] == 0:
    print('NO')
else:
    for i in range(1, len(ans)):
        print(ans[i])
