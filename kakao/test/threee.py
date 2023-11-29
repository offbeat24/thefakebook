from itertools import combinations, product
def calculate_win(a_combo, b_combo):
    win = 0

    a_result = product(*a_combo)
    b_result = product(*b_combo)
    i = 0
    for a in a_result:
        b_result = product(*b_combo)
        for b in b_result:
          if sum(a) > sum(b):
            win += 1
    return win

def solution(dice):
    n = len(dice)
    max_win_prob = -1
    best_combination = []

    for a_combo in combinations(range(n), n//2):
        b_combo = set(range(n)) - set(a_combo)
        win_prob = calculate_win([dice[i] for i in a_combo], [dice[i] for i in b_combo])
        if win_prob > max_win_prob:
            max_win_prob = win_prob
            best_combination = a_combo
    
    return sorted([i+1 for i in best_combination])

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]

print(solution(dice))