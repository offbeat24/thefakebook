def solution(survey, choices):
    answer = ''
    personality = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }
    for idx, q in enumerate(survey):
        if choices[idx] > 4:
            personality[q[1]] += (choices[idx] - 4)
        elif choices[idx] < 4:
            personality[q[0]] += (4 - choices[idx])

    if personality['R'] >= personality['T']:
        answer += 'R'
    if personality['R'] < personality['T']:
        answer += 'T'
    if personality['C'] >= personality['F']:
        answer += 'C'
    if personality['C'] < personality['F']:
        answer += 'F'
    if personality['J'] >= personality['M']:
        answer += 'J'
    if personality['J'] < personality['M']:
        answer += 'M'
    if personality['A'] >= personality['N']:
        answer += 'A'
    if personality['A'] < personality['N']:
        answer += 'N'

    return answer
