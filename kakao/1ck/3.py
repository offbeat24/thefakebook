def solution(alp, cop, problems):
    answer = 0
    problems.sort(key=lambda x: (x[0]+x[1]-alp-cop, x[4]))
    for problem in problems:

    return answer
