n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]


tetrominoes = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # O
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # I
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # L
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # S
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # T
    [(0, 0), (1, 0), (1, -1), (2, -1)], # Z
    [(0, 0), (1, 0), (2, 0), (2, -1)]  # J
]

def check(x, y):
    global max_score
    for tetromino in tetrominoes:
        for dx, dy in tetromino:
            if not (0 <= x + dx < n and 0 <= y + dy < m):
                break
        else:  # 모든 블록이 보드 안에 있을 경우
            score = sum(board[x + dx][y + dy] for dx, dy in tetromino)
            max_score = max(max_score, score)

max_score = 0
for i in range(n):
    for j in range(m):
        check(i, j)

print(max_score)
