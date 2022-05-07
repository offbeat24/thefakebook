from collections import deque


def solution(rc, operations):
    answer = rc
    n = len(rc)
    m = len(rc[0])
    for op in operations:
        if op == "ShiftRow":
            answer = shift_row(answer)
            print(answer)
            continue
        if op == "Rotate":
            answer = rotate(answer, n, m)
            print(answer)
            continue
    return answer


def shift_row(rc):
    dq_rc = deque(rc)
    dq_rc.appendleft(dq_rc.pop())

    return list(dq_rc)


def rotate(rc, n, m):
    rc_result = [[0]*m for _ in range(n)]

    for i in range(0, n):
        for j in range(0, m):
            if (i == 0) & (j > 0):
                rc_result[0][j] = rc[0][j-1]
            elif (i > 0) & (j == (m-1)):
                rc_result[i][j] = rc[i-1][j]
            elif (i == (n-1)) & (j < (m-1)):
                rc_result[i][j] = rc[i][j+1]
            elif (i < (n-1)) & (j == 0):
                rc_result[i][j] = rc[i+1][j]
            else:
                rc_result[i][j] = rc[i][j]

    return rc_result


print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
      ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
