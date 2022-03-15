n = int(input())

chess = [0] * n
visited = [0] * n
answer = 0


def queen(depth):
    global answer

    if depth == n:
        answer += 1
        return

    for i in range(n):
        if visited[i] == 0:
            chess[depth] = i

            for j in range(depth):
                if abs(chess[depth] - chess[j]) == abs(depth - j):
                    break
            else:
                visited[i] = 1
                queen(depth+1)
                visited[i] = 0


queen(0)
print(answer)
