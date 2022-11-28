def solution(s, times):
    answer = []
    days = list()
    start = s.split(':')
    days.append(start)
    for idx, time in enumerate(times) :
        t = time.split(':')
        day = [0 for _ in range(6)]
        day[5] = days[idx][5] + t[3]
        day[4] = days[idx][4] + t[2]
        day[3] = days[idx][3] + t[1]
        day[2] = days[idx][2] + t[0]
        day[1] = days[idx][1]
        day[0] = days[idx][0]
        if day[5] >= 60 :
            day[4] += 1
            day[5] -= 60
        if day[4] >= 60 :
            day[3] += 1
            day[4] -= 60
        if day[3] >= 24 :
            day[2] += 1
            day[3] -= 24
        if day[2] > 30 :
            day[1] += 1
            day[2] -= 30
        if day[1] > 12 :
            day[0] += 1
            day[1] -= 12
        days.append(day)
    return answer