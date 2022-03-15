n = int(input())

numbers = list(map(int, input().split()))

opr_input = list(map(int, input().split()))

max_ = float('-inf')

min_ = float('inf')

opr = list()

tmp_opr = list()

visited = [0] * (n-1)
for idx, i in enumerate(opr_input):
    for j in range(i):
        opr.append(idx)


def calc():
    answer = numbers[0]
    i = 1
    for o in tmp_opr:
        if o == 0:
            answer += numbers[i]
            i += 1
        elif o == 1:
            answer -= numbers[i]
            i += 1
        elif o == 2:
            answer *= numbers[i]
            i += 1
        elif o == 3:
            answer = int(answer / numbers[i])
            i += 1
    return answer


def inserting(depth):
    global min_
    global max_
    if depth == n-1:
        answer = calc()
        min_ = min(min_, answer)
        max_ = max(max_, answer)
        return

    for i in range(n-1):
        if visited[i] == 0:
            visited[i] = 1
            tmp_opr.append(opr[i])
            inserting(depth+1)
            tmp_opr.pop()
            visited[i] = 0


inserting(0)
print(max_, min_, sep='\n')
