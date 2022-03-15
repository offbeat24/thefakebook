n = 20
team_sep = [1, 1, 2, 2]
visited = [0] * n
team = list()


def seperating(depth, idx):
    if depth == n//2:
        print(team)
        return
        #answer = min(answer, calc())
    for i in range(idx, n):
        if i not in team:
            team.append(i)
            seperating(depth + 1, idx + 1)
            team.pop()


seperating(0, 0)
